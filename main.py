from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime

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
async def honeypot(
    event: ScamEvent,
    request: Request,
    authorization: str = Header(None)
):
    
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    client_ip = request.client.host
    user_agent = request.headers.get("user-agent")

    scam_detected = detect_scam(event.message)

    response = {
        "timestamp": datetime.utcnow().isoformat(),
        "source_ip": client_ip,
        "user_agent": user_agent,
        "message_received": event.message,
        "scam_detected": scam_detected,
    }

   
    if scam_detected:
        response["handoff"] = "ai_agent"
        response["agent_reply"] = ai_agent_response(event.message)
    else:
        response["handoff"] = "none"
        response["agent_reply"] = None

    return response
