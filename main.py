from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

API_KEY = "guvi123"

class ScamRequest(BaseModel):
    message: str

@app.post("/honeypot")
def honeypot(
    data: ScamRequest,
    x_api_key: str = Header(None, alias="x-api-key")
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    msg = data.message.lower()
    scam_keywords = ["otp", "bank", "blocked", "urgent", "lottery"]

    scam_detected = any(word in msg for word in scam_keywords)

    return {
        "scam_detected": scam_detected,
        "handoff": "ai_agent" if scam_detected else "none"
    }
