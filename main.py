import os, sys
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("API_KEY")
ticker = ""
datatype = "json"

base_url_key_metrics = f"https://fmpcloud.io/api/v3/key-metrics-ttm/{ticker}?datatype={datatype}&apikey={api_key}"
base_url_financial_ratios = f"https://fmpcloud.io/api/v3/ratios/{ticker}?datatype={datatype}&apikey={api_key}"
