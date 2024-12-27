from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TARGET_SERVER_URL = "http://127.150.151.263:8000/log"

@app.get("/send")
async def send_data():
    data = [
        {"coin": 100}
    ]
    
    async with httpx.AsyncClient() as client:
        response = await client.post(TARGET_SERVER_URL, json=data)
    
    return {"status": response.status_code, "response": response.json()}
