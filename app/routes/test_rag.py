from fastapi import APIRouter

from app.rag.text_processor import (
    read_text_file,
    chunk_text
)


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.get("/test")

def test_rag():

    text = read_text_file(
        "uploads/test.txt"
    )

    chunks = chunk_text(text)

    return {
        "total_chunks": len(chunks),
        "first_chunk": chunks[0] if chunks else None
    }