from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":

    # Load documents
    docs = load_all_documents("data")

    # Create FAISS vector store
    store = FaissVectorStore("faiss_store")

    # Build FAISS index (first run only)
    store.build_from_documents(docs)

    # Initialize RAG search
    rag_search = RAGSearch()

    # Ask a question
    query = "Information security risk assessment"

    summary = rag_search.search_and_summarize(
        query,
        top_k=3
    )

    print("Summary:", summary)