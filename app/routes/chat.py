from fastapi import (
    APIRouter,
    Depends
)

from app.auth.dependencies import get_current_user

from app.models.user import User

from app.rag.retriever import (
    retrieve_relevant_chunks
)


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/ask")
def ask_question(
    query: str,
    current_user: User = Depends(get_current_user)
):

    chunks = retrieve_relevant_chunks(query)

    return {
        "question": query,
        "retrieved_chunks": chunks
    }