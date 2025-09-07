# Geo Compliance Classifier

## Problem Statement
Automated pipeline that classifies new product features for compliance with global regulations. Given a feature title and description, the system retrieves relevant legal texts, verifies jurisdictional alignment, and outputs a triage label (Yes/No/Uncertain) along with an audit trail.

## Features and Functionality
- **Agent pipeline:** query preparation, domain retrieval, reranking, verification, optional human-in-the-loop review, aggregation and classification.
- **Jurisdiction-aware retrieval:** domain agents search a curated knowledge base of regional regulations.
- **Transparent outputs:** final decisions include reasoning, cited regulations and an audit trail.
- **Demo:** run `python main.py` for a local example.

![Alt text](assets/atechjam_archi-1.png)

## Development Tools
- Python 3.x
- Git & VS Code

## APIs
- OpenAI API for language models and embeddings
- Hugging Face models for reranking

## Libraries
- LangChain & LangChain Community
- ChromaDB
- NLTK
- NumPy
- Pydantic
- Rank-BM25
- Requests
- Python Dotenv

## Assets
- `assets/atechjam_archi-1.png` – high level agent workflow diagram

## Datasets
- Regulatory text snippets under `kb/` (e.g., GDPR, EU DSA, PDPA, youth safety laws)

## Repository
This project is open sourced at: [Geo Compliance Classifier Repository](https://github.com/your-team/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-)

### Local Demo Setup
1. Clone the repository
   ```bash
   git clone https://github.com/your-team/Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-.git
   cd Tiktok-Techjam-Geo-Compliance-Classifier-WalaWalaOokOok-
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Provide an `OPENAI_API_KEY` in your environment
4. Run the demo
   ```bash
   python main.py
   ```
