import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()

collection = client.create_collection(
    name="my_docs",
    embedding_function=embedding_fn
)

collection.add(
    documents=[
        "Python is a programming language",
        "Machine learning uses data to train models",
        "Kathmandu is the capital of Nepal",
        "Deep learning uses neural networks",
        "Nepal is a beautiful country"
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

results = collection.query(
    query_texts=["How does AI learn?"],
    n_results=2
)

print(results["documents"])