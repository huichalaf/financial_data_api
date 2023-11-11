import os, sys
import dotenv
import requests
import asyncio
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
auth_token = os.getenv("AUTH_TOKEN")
ticker = ""
datatype = "json"

base_url_key_metrics = f"https://fmpcloud.io/api/v3/key-metrics-ttm/{ticker}?datatype={datatype}&apikey={api_key}"
base_url_financial_ratios = f"https://fmpcloud.io/api/v3/ratios/{ticker}?datatype={datatype}&apikey={api_key}"

app = FastAPI()
API_KEY_NAME = "WALLSTREETGPT-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Dependencia que verifica la API key
def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != auth_token:
        raise HTTPException(status_code=401, detail="Unauthorized")

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

@app.post("//auth")
async def auth(api_key: str = Depends(validate_api_key)):
    return {"success": True}

@app.post("//key_metrics")
async def key_metrics(request: Request,  api_key: str = Depends(validate_api_key)):
    data = await request.json()
    ticker = data["ticker"]
    base_url_key_metrics = f"https://fmpcloud.io/api/v3/key-metrics-ttm/{ticker}?datatype={datatype}&apikey={api_key}"
    response = requests.get(base_url_key_metrics)
    return response.json()

@app.post("//financial_ratios")
async def financial_ratios(request: Request, api_key: str = Depends(validate_api_key)):
    data = await request.json()
    ticker = data["ticker"]
    base_url_financial_ratios = f"https://fmpcloud.io/api/v3/ratios/{ticker}?datatype={datatype}&apikey={api_key}"
    response = requests.get(base_url_financial_ratios)
    return response.json()

@app.post("//quote")
async def quote(request: Request, api_key: str = Depends(validate_api_key)):
    data = await request.json()
    ticker = data["ticker"]
    base_url_quote = f"https://fmpcloud.io/api/v3/quote/{ticker}?datatype={datatype}&apikey={api_key}"
    response = requests.get(base_url_quote)
    return response.json()

@app.post("//technical_indicators")
async def technical_indicators(request: Request, api_key: str = Depends(validate_api_key)):
    #SMA - EMA - WMA - DEMA - TEMA - williams - RSI - ADX - standardDeviation
    data = await request.json()
    ticker = data["ticker"]
    indicator = data["indicator"]
    period = data["period"]
    # url = https://fmpcloud.io/api/v3/technical_indicator/daily/AAPL?period=10&type=ema&apikey=c8a7ba8496a4eb4c302aafb9eb6eeea2
    base_url_technical_indicators = f"https://fmpcloud.io/api/v3/technical_indicator/daily/{ticker}?period={period}&type={indicator}&apikey={api_key}"
    response = requests.get(base_url_technical_indicators)
    return response.json()

@app.post("//forex_quote")
async def forex_quote(request: Request, api_key: str = Depends(validate_api_key)):
    #https://fmpcloud.io/api/v3/historical-price-full/JPYUSD?timeseries=5&apikey=c8a7ba8496a4eb4c302aafb9eb6eeea2
    data = await request.json()
    ticker = data["ticker"]
    base_url_forex_quote = f"https://fmpcloud.io/api/v3/historical-price-full/{ticker}?timeseries=5&apikey={api_key}"
    response = requests.get(base_url_forex_quote)
    return response.json()

@app.post("//crypto_quote")
async def crypto_quote(request: Request, api_key: str = Depends(validate_api_key)):
    #https://fmpcloud.io/api/v3/historical-price-full/BTCUSD?timeseries=5&apikey=c8a7ba8496a4eb4c302aafb9eb6eeea2
    data = await request.json()
    ticker = data["ticker"]
    base_url_crypto_quote = f"https://fmpcloud.io/api/v3/historical-price-full/{ticker}?timeseries=5&apikey={api_key}"
    response = requests.get(base_url_crypto_quote)
    return response.json()



if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="0.0.0.0", port=8080))