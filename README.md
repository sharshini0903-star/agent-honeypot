Problem Statement:
Online scams like fake bank alerts, OTP fraud, and lottery messages are increasing rapidly. Existing systems often fail to safely capture scam interactions or respond automatically.

Solution:
This project implements a secure, cloud-hosted honeypot API that:
1.Receives scam messages
2.Detects scam intent
3.Hands off the interaction to an autonomous AI agent
4.Prevents victim engagement while collecting intelligence

Key Features:
1.Secure API with Bearer Token authentication
2.Honeypot endpoint for scam interactions
3.Scam detection using keyword-based analysis
4.AI agent handoff with safe responses
5.Public deployment using Render (Free Tier)

API Details:
Endpoint:
POST /honeypot

Headers:
Authorization: Bearer <API_KEY>
Content-Type: application/json

Request:
{
  "message": "Your bank account is blocked. Share OTP immediately"
}

Response (Scam Detected)
{
  "scam_detected": true,
  "handoff": "ai_agent",
  "agent_reply": "Never share OTP or UPI details."
}

Live API:
https://agent-honeypot.onrender.com

Tech Stack:
1.FastAPI (Python)
2.Uvicorn
3.Render (Cloud)

Author:
Harshini S
