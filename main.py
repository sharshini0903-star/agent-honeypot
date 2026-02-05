from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

API_KEY = "guvi123"

class Message(BaseModel):
    sender: str
    text: str
    timestamp: int

class RequestBody(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[Any]
    metadata: Dict[str, Any]

@app.post("/honeypot")
def honeypot(
    data: RequestBody,
    x_api_key: str = Header(None, alias="x-api-key")
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    scam_text = data.message.text.lower()
    keywords = ["otp", "bank", "blocked", "verify", "urgent"]

    if any(word in scam_text for word in keywords):
        reply = "Why is my account being suspended?"
    else:
        reply = "Can you provide more details?"

    return {
        "status": "success",
        "reply": reply
    }

@app.get("/")
def health():
    return {"status": "running"}
