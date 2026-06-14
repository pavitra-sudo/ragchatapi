from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.scraper import scrape_url
from app.rag import ingest_text, chat_with_context

app = FastAPI(title="RAG Chat API")

class IngestRequest(BaseModel):
    url: str

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/ingest")
def ingest_url(request: IngestRequest):
    text = scrape_url(request.url)
    if not text:
        raise HTTPException(status_code=400, detail="Failed to scrape URL or URL is empty.")
    
    try:
        ingest_text(text)
        return {"message": "URL successfully ingested."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error ingesting text: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        answer = chat_with_context(request.query)
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.get("/")
def read_root():
    return {"message": "Welcome to RAG Chat API. Use /ingest and /chat endpoints."}
