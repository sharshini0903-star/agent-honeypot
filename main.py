from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from datetime import datetime
from fastapi import Depends


app = FastAPI()

API_KEY = "guvi-secret-key"  


class ScamEvent(BaseModel):
    message: str


def detect_scam(message: str) -> bool:
    scam_keywords = [
        "upi",
        "otp",
        "bank",
        "urgent",
        "lottery",
        "free money",
        "account blocked"
    ]
    message_lower = message.lower()
    return any(keyword in message_lower for keyword in scam_keywords)


def ai_agent_response(message: str) -> str:
    return (
        "Hello! For security reasons, please contact our official support "
        "through the bank’s registered website. Never share OTP or UPI details."
    )


@app.post("/honeypot")
def honeypot(data: ScamRequest, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    message = data.message.lower()

    scam_keywords = ["otp", "bank", "blocked", "urgent", "lottery"]

    scam_detected = any(word in message for word in scam_keywords)

    return {
        "scam_detected": scam_detected,
        "handoff": "ai_agent" if scam_detected else "none"
    }
