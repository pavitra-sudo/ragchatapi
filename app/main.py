from fastapi import FastAPI

from app.database import Base, engine
from app.routes.user import router as user_router
from app.routes.test_rag import router as rag_router
from app.routes.document import router as document_router
from app.routes.chat import router as chat_router



Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RAG Chat API"
)

app.include_router(user_router)
app.include_router(chat_router)
app.include_router(document_router)
app.include_router(rag_router)


@app.get("/")
async def root():
    return {
        "message": "RAG Chat API Running"
    }