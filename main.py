import os, sys
import dotenv
import requests
import asyncio
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
auth_token = os.getenv("AUTH_TOKEN")
ticker = ""
datatype = "json"

base_url_key_metrics = f"https://fmpcloud.io/api/v3/key-metrics-ttm/{ticker}?datatype={datatype}&apikey={api_key}"
base_url_financial_ratios = f"https://fmpcloud.io/api/v3/ratios/{ticker}?datatype={datatype}&apikey={api_key}"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def status():
    return {"success": True}

@app.post("/auth")
async def auth(request: Request):
    data = await request.json()
    if data["auth_token"] == auth_token:
        return {"success": True}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
@app.post("/key_metrics")
async def key_metrics(request: Request):
    data = await request.json()
    ticker = data["ticker"]
    base_url_key_metrics = f"https://fmpcloud.io/api/v3/key-metrics-ttm/{ticker}?datatype={datatype}&apikey={api_key}"
    response = requests.get(base_url_key_metrics)
    return response.json()

@app.post("/financial_ratios")
async def financial_ratios(request: Request):
    data = await request.json()
    ticker = data["ticker"]
    base_url_financial_ratios = f"https://fmpcloud.io/api/v3/ratios/{ticker}?datatype={datatype}&apikey={api_key}"
    response = requests.get(base_url_financial_ratios)
    return response.json()

if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="0.0.0.0", port=8000))