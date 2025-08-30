import nltk
import openai
import os
import re
from pathlib import Path
from dotenv import load_dotenv
from nltk.tokenize import sent_tokenize
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import List

nltk.download('punkt')

project_root = Path(__file__).resolve().parent.parent
dotenv_path = project_root / '.env'
load_dotenv(dotenv_path=dotenv_path)

apikey = os.environ.get("OPENAI_API_KEY")
# print(apikey)

# _file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\CA_SB967.txt"
_file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\FL_HB3.txt"

class Chunk(BaseModel):
    """Chunk with chunk_index and sentence_indices"""
    chunk_index: int = Field(description="Integer chunk_index starting at 0")
    sentence_indices: List[int] = Field(
        description="Ordered sentence_indices that belong to this chunk"
    )

class SemanticChunks(BaseModel):
    """List of chunks"""
    chunks: List[Chunk] = Field(
        description="List of chunks; each has a chunk_index and its sentence_indices"
    )

def open_txt(txtfile):
    try:
        with open(txtfile, 'r', encoding='utf-8') as file:
            text = file.read()

        # Split to get title and content using your pattern
        if '/()/()/\n\n\n' in text:
            parts = text.split('/()/()/\n\n\n', 1)
            title = parts[0].strip()
            content = parts[1].strip()
            return title, content
        else:
            # Fallback if pattern not found
            print(f"Pattern not found in {txtfile}, using first line as title")
            lines = text.split('\n', 1)
            title = lines[0].strip()
            content = lines[1] if len(lines) > 1 else ""
            return title, content
            
    except Exception as e:
        print(f"Error reading {txtfile}: {e}")
        return None, None

# Initialize structured llm function
def init_llm():
    if (hf_token := config.get_token()):
        llm = HuggingFaceEndpoint(
            repo_id='openai/gpt-oss-20b',
            huggingfacehub_api_token = hf_token
        )
        
        llm = ChatHuggingFace(llm = llm, temperature = 0)
        structured_llm = llm.bind_tools([SemanticChunks])
        return structured_llm
    try:
        llm = init_chat_model("gpt-4o-mini", model_provider="openai")
        structured_llm = llm.with_structured_output(SemanticChunks)
        return structured_llm
    except openai.APIError as e:
        print(f"An API error occurred: {e}")


def split_and_index_doc(legi_doc_txt: str):
    legi_title, legi_doc = open_txt(legi_doc_txt)
    if not legi_doc or not legi_doc.strip():
        # make cause obvious to caller
        raise ValueError(f"Empty or unreadable file: {legi_doc_txt}")

    # normalize newlines
    legi_doc = legi_doc.replace("\r\n", "\n").replace("\r", "\n")

    # primary sentence split
    legi_doc_split = sent_tokenize(legi_doc)

    # fallback if tokenizer yields nothing
    if not legi_doc_split:
        # split on punctuation or newlines as a last resort
        legi_doc_split = [s.strip() for s in re.split(r'(?<=[\.\?\!])\s+|\n+', legi_doc) if s.strip()]

    # still nothing? raise
    if not legi_doc_split:
        raise ValueError(f"No sentences tokenized for: {legi_doc_txt}")

    sentence_idx = {}
    legi_doc_split_idxed = []
    for i, sentence in enumerate(legi_doc_split):
        legi_doc_split_idxed.append(f"<{i}>{sentence}</{i}>")
        sentence_idx[i] = sentence

    out_str = " ".join(legi_doc_split_idxed)
    return legi_title, out_str, sentence_idx


def get_chunks(doc, model=None):
    if not model:
        model = init_llm()

    law_name, processed_doc, reconstruction_index = split_and_index_doc(doc)

    # if somehow empty, bail out early (caller can skip file)
    if not reconstruction_index:
        return law_name, []

    chunking_prompt = ChatPromptTemplate.from_template(
        """You are an expert at splitting text into smaller chunks without breaking context.
        Each sentence in the input has a numeric index in <index>sentence</index> tags.
        Return ONLY the fields defined in the SemanticChunks schema.

        Rules:
        - Keep sentences in original order within each chunk.
        - Do not skip indices you include; no duplicates within a chunk.
        - Prefer 2-3 sentences per chunk if sentences are short, but just 1-2 if sentences are long.

        Text to split:
        {text}"""
    )

    chunking_prompt_w_text = chunking_prompt.invoke({"text": processed_doc})
    chunks = model.invoke(chunking_prompt_w_text)
    if (hf_token := config.get_token()):
        chunks = SemanticChunks.model_validate(chunks.tool_calls[0]['args'])

    reconstructed_chunks = []

    # (optional) keep your prints if you like
    # print(reconstruction_index.keys())
    for chunk in chunks.chunks:
        # print(chunk)
        chunk_sentences = []
        for sentence_idx in chunk.sentence_indices:
            # **GUARD**: only append if index exists
            if sentence_idx in reconstruction_index:
                chunk_sentences.append(reconstruction_index[sentence_idx])
            # else silently skip bad indices from the model
        if chunk_sentences:
            reconstructed_chunks.append(" ".join(chunk_sentences))

    # If the model returned only bad indices, make a single fallback chunk
    if not reconstructed_chunks:
        reconstructed_chunks = [" ".join(reconstruction_index[i] for i in sorted(reconstruction_index))]

    return law_name, reconstructed_chunks
