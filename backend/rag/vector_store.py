import chromadb

# In-memory vector database (NO file locking, NO Windows errors)
client = chromadb.EphemeralClient()

collection = client.get_or_create_collection(
    name="faqs",
    metadata={"hnsw:space": "cosine"}
)

def add_faq(question: str, answer: str, embedding: list):
    collection.add(
        ids=[question],
        documents=[question],
        embeddings=[embedding],
        metadatas=[{"answer": answer}]
    )

def search_faq(query_embedding: list, k=3):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
