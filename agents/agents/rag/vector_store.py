from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings

def create_vector_store(text: str):
    """
    Splits text into chunks, generates embeddings using Ollama,
    and stores them in a FAISS vector database.
    """

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    # Wrap chunks as Documents
    docs = [Document(page_content=t) for t in chunks]

    # Generate embeddings using Ollama
    embeddings = OllamaEmbeddings(model="llama3:instruct")

    # Create FAISS vector store
    db = FAISS.from_documents(docs, embeddings)
    

    return db