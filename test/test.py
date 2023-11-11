import requests
import dotenv
import os

# Load the environment variables
dotenv.load_dotenv()

# The base URL where your FastAPI application is running
BASE_URL = "https://assistants-api-aidtogrow.fly.dev/"

# Define the ticker symbol you want to test
ticker_to_test = 'AAPL'

# Define the auth token for testing purposes
auth_token_to_test = os.getenv("AUTH_TOKEN")  # Replace with your actual auth token

# Define the name of the API key header
API_KEY_HEADER_NAME = "WALLSTREETGPT-API-KEY"

# Function to perform a test authentication
def test_auth():
    url = f"{BASE_URL}/auth"
    headers = {API_KEY_HEADER_NAME: auth_token_to_test}
    response = requests.post(url, headers=headers)
    if response.ok:
        print("Authentication successful.")
    else:
        print(f"Authentication failed: {response.status_code} {response.text}")

# Function to test the 'key_metrics' endpoint
def test_key_metrics(ticker):
    url = f"{BASE_URL}/key_metrics"
    headers = {API_KEY_HEADER_NAME: auth_token_to_test}
    response = requests.post(url, headers=headers, json={"ticker": ticker})
    if response.ok:
        return response.json()
    else:
        raise Exception(f"Error fetching key metrics: {response.status_code} {response.text}")

# Function to test the 'financial_ratios' endpoint
def test_financial_ratios(ticker):
    url = f"{BASE_URL}/financial_ratios"
    headers = {API_KEY_HEADER_NAME: auth_token_to_test}
    response = requests.post(url, headers=headers, json={"ticker": ticker})
    if response.ok:
        return response.json()
    else:
        raise Exception(f"Error fetching financial ratios: {response.status_code} {response.text}")

# Run the tests
test_auth()
print("Key Metrics:", test_key_metrics(ticker_to_test))
print("Financial Ratios:", test_financial_ratios(ticker_to_test))
