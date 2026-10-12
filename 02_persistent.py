import chromadb
from chromadb.utils import embedding_functions

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="my_docs",
    embedding_function=embedding_fn
)

collection.add(
    documents=[
        "Python is a programming language",
        "Machine learning uses data",
        "Nepal is in Asia"
        "Javascript is a programming language"
    ],
    metadatas=[
        {"source": "tech"},
        {"source": "ai"},
        {"source": "geo"}
    ],
    ids=["1", "2", "3"]
)

results = collection.query(
    query_texts=["programming language"],
    n_results=2
)

print("Documents:", results["documents"])
print("Metadata:", results["metadatas"])