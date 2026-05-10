from fastapi import FastAPI

from app.database import Base, engine
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RAG Chat API"
)


@app.get("/")
async def root():
    return {
        "message": "Database connected successfully"
    }