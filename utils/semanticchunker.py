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

nltk.download('punkt')

project_root = Path(__file__).resolve().parent.parent
dotenv_path = project_root / '.env'
load_dotenv(dotenv_path=dotenv_path)

apikey = os.environ.get("OPENAI_API_KEY")
# print(apikey)

# _file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\CA_SB967.txt"
_file = "C:\\Users\\Teh Ze Shi\\OneDrive\\schoolwork\TT Techjam 2025\\lol\\kb\\youth_safety\\FL_HB3.txt"

class Chunk(BaseModel):
    id: int = Field(description="Chunk index starting at 0")
    sentence_ids: list[int] = Field(
        description="Ordered sentence indices that belong to this chunk"
    )

class SemanticChunks(BaseModel):
    chunks: list[Chunk] = Field(
        description="List of chunks; each has an id and its sentence indices"
    )

def open_txt(txtfile):
    try:
        file = open(txtfile, encoding='utf-8')
        return file.read()
    except Exception as e:
        print(e)
        return None

# Initialize structured llm function
def init_llm():
    try:
        llm = init_chat_model("gpt-4o-mini", model_provider="openai")
        structured_llm = llm.with_structured_output(SemanticChunks)
        return structured_llm
    except openai.APIError as e:
        print(f"An API error occurred: {e}")


def split_and_index_doc(legi_doc_txt: str):
    legi_doc = open_txt(legi_doc_txt)
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
    return out_str, sentence_idx


def get_chunks(doc, model=None):
    if not model:
        model = init_llm()

    processed_doc, reconstruction_index = split_and_index_doc(doc)

    # if somehow empty, bail out early (caller can skip file)
    if not reconstruction_index:
        return []

    chunking_prompt = ChatPromptTemplate.from_template(
        """You are an expert at splitting text into smaller chunks without breaking context.
        Each sentence in the input has a numeric index in <index>sentence</index> tags.
        Return ONLY the fields defined in the SemanticChunking schema.

        Rules:
        - Keep sentences in original order within each chunk.
        - Do not skip indices you include; no duplicates within a chunk.
        - Prefer 1-2 sentences per chunk if sentences are short, but just 1 if sentences are long.

        Text to split:
        {text}"""
    )

    chunking_prompt_w_text = chunking_prompt.invoke({"text": processed_doc})
    chunks = model.invoke(chunking_prompt_w_text)

    reconstructed_chunks = []

    # (optional) keep your prints if you like
    # print(reconstruction_index.keys())
    for chunk in chunks.chunks:
        print(chunk)
        chunk_sentences = []
        for sentence_idx in chunk.sentence_ids:
            # **GUARD**: only append if index exists
            if sentence_idx in reconstruction_index:
                chunk_sentences.append(reconstruction_index[sentence_idx])
            # else silently skip bad indices from the model
        if chunk_sentences:
            reconstructed_chunks.append(" ".join(chunk_sentences))

    # If the model returned only bad indices, make a single fallback chunk
    if not reconstructed_chunks:
        reconstructed_chunks = [" ".join(reconstruction_index[i] for i in sorted(reconstruction_index))]

    return reconstructed_chunks