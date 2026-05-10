from app.rag.embeddings import generate_embedding
from app.rag.vector_store import collection


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 3
):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results.get("documents", [])

    if not documents:
        return []

    return documents[0]