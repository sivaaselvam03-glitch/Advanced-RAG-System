# 📚 Advanced RAG System using FAISS, LangChain & Groq

An end-to-end **Retrieval-Augmented Generation (RAG)** application that performs semantic search over multiple document formats using **FAISS** and **Sentence Transformers**, then generates accurate responses with **Groq's Llama 3.1** model.

The project supports automatic document ingestion, embedding generation, vector indexing, semantic retrieval, and AI-powered summarization.

---

## 🚀 Features

- 📄 Multi-format document loading
  - PDF
  - TXT
  - CSV
  - Excel
  - Word
  - JSON

- ✂️ Automatic text chunking
- 🧠 Sentence Transformer embeddings
- ⚡ FAISS vector database
- 🔍 Semantic similarity search
- 🤖 Groq Llama 3.1 LLM integration
- 📑 Context-aware answer generation
- 📝 AI-powered document summarization
- 💾 Persistent vector database
- ⚙️ Modular and scalable project architecture

---

# 🏗️ Project Architecture

```
                    Documents
                        │
                        ▼
              Document Loader
                        │
                        ▼
               Text Chunking
                        │
                        ▼
          Sentence Transformer
        (all-MiniLM-L6-v2)
                        │
                        ▼
                 Embeddings
                        │
                        ▼
             FAISS Vector Store
                        │
                        ▼
             Semantic Retrieval
                        │
                        ▼
            Relevant Context
                        │
                        ▼
           Groq Llama 3.1 LLM
                        │
                        ▼
        Answer / Summary Generation
```

---

# 🛠️ Tech Stack

- Python
- LangChain
- FAISS
- Sentence Transformers
- Hugging Face
- Groq API
- NumPy
- Pandas
- python-dotenv

---

# 📂 Project Structure

```
RAG/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   ├── iso27001.pdf
│   └── text_files/
│
├── faiss_store/
│   ├── faiss.index
│   └── metadata.pkl
│
├── notebook/
│   ├── doc.ipynb
│   └── pdf_loader.ipynb
│
└── src/
    ├── __init__.py
    ├── data_loader.py
    ├── embedding.py
    ├── vectorstore.py
    └── search.py
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/advanced-rag.git

cd advanced-rag
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

Using pip

```bash
pip install -r requirements.txt
```

Using uv

```bash
uv add -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run the Project

```bash
python app.py
```

---

# 💡 Example Query

```
Information security risk assessment
```

### Output

```
The organization shall define and apply an information security risk assessment process that:

• Establishes information security risk criteria.
• Identifies risks related to confidentiality, integrity, and availability.
• Analyzes the likelihood and consequences of identified risks.
• Determines risk treatment options.
• Maintains documented information.
```

---

# 🔄 Workflow

```
Load Documents
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS
        │
        ▼
User Query
        │
        ▼
Semantic Search
        │
        ▼
Retrieve Top-K Chunks
        │
        ▼
Prompt Construction
        │
        ▼
Groq LLM
        │
        ▼
Generated Response
```

---

# 📌 Supported File Types

- PDF
- TXT
- CSV
- Excel (.xlsx)
- Word (.docx)
- JSON

---

# 🎯 Future Improvements

- Hybrid Search (BM25 + Vector Search)
- Cross Encoder Reranking
- Chat Memory
- Source Citations
- Streaming Responses
- Streamlit UI
- FastAPI Backend
- RAG Evaluation (RAGAS)
- Docker Deployment
- Hugging Face Spaces Deployment

---

# 📖 Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Dense Embeddings
- Prompt Engineering
- Large Language Models
- Information Retrieval
- FAISS Indexing
- LangChain Integration
- Document Processing Pipeline

---

# 👨‍💻 Author

**Siva Selvam**

**Aspiring AI Engineer | Machine Learning Engineer | Data Scientist**

### Skills

- Python
- Machine Learning
- LangChain
- LLMs
- RAG
- FAISS
- Sentence Transformers
- SQL
- Pandas
- NumPy

---

# ⭐ If you found this project useful, please consider giving it a Star.
