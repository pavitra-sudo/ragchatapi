from app.rag.embeddings import generate_embedding
from app.rag.vector_store import collection


def ingest_chunks(
    chunks: list[str],
    document_id: int
):

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        collection.add(
            documents=[chunk],

            embeddings=[embedding],

            ids=[f"{document_id}_{index}"],

            metadatas=[
                {
                    "document_id": document_id,
                    "chunk_index": index
                }
            ]
        )