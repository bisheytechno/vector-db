import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

# Setup
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client     = chromadb.PersistentClient(path="./chroma_db_pipeline")
collection = client.get_or_create_collection(
    name="knowledge_base",
    embedding_function=embedding_fn
)

# Documents — Knowledge base
docs = [
    "Python is used for AI and data science",
    "Machine learning trains models on data",
    "Nepal has beautiful mountains and culture",
    "LLMs use transformer architecture",
    "Kathmandu is Nepal's capital city",
    "ChromaDB is a vector database for AI",
    "RAG combines search with language models",
    "FastAPI is used to build AI backends"
]

# Store!
collection.add(
    documents=docs,
    metadatas=[{"id": i} for i in range(len(docs))],
    ids=[f"doc{i}" for i in range(len(docs))]
)

print(f"✅ Stored {collection.count()} documents!")

# Search function
def search(query, n=2):
    results = collection.query(
        query_texts=[query],
        n_results=n
    )
    print(f"\nQuery: {query}")
    for doc in results["documents"][0]:
        print(f" -> {doc}")

# Test!
search("How does AI learn?")
search("Tell me about Nepal")
search("What is Python used for?")
search("How to build AI API?")