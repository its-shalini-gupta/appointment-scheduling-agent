from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import chat, calendly_integration

app = FastAPI(title="Appointment Scheduling Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(calendly_integration.router, prefix="/api/calendly", tags=["calendly"])

@app.get("/")
def home():
    return {"status": "Backend running"}
