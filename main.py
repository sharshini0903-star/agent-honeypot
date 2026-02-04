from fastapi import FastAPI, Header, HTTPException, Request
from datetime import datetime

app = FastAPI()

API_KEY = "honeypot_secret_key"

@app.get("/honeypot")
async def honeypot_endpoint(
    request: Request,
    authorization: str = Header(None)
):
    if not authorization or authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    client_ip = request.client.host if request.client else "unknown"
    user_agent = request.headers.get("user-agent", "unknown")

    return {
        "status": "active",
        "message": "Honeypot endpoint reached successfully",
        "timestamp": datetime.utcnow().isoformat(),
        "intelligence": {
            "source_ip": client_ip,
            "user_agent": user_agent,
            "interaction_type": "probe"
        }
    }
