from fastapi import APIRouter
from pydantic import BaseModel
from backend.agent.scheduling_agent import process_message
from backend.rag.faq_rag import answer_faq

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str
    meta: dict | None = None

@router.post("/", response_model=ChatResponse)
def chat(req: ChatRequest):
    faq = answer_faq(req.message)
    if faq:
        return ChatResponse(reply=faq)

    reply, meta = process_message(req.message, {})
    return ChatResponse(reply=reply, meta=meta)
