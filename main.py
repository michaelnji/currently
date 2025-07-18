from enum import Enum
import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv
from functions.convert import convert_currency
from functions.currencies import fetchCurrencies
from pydantic import BaseModel

load_dotenv()
API_KEY = os.getenv('CURRENCY_KEY')

app = FastAPI()

# for server health
@app.get('/status')
def get_status()-> str:
    return 'App is running well. Exchange rates provided by UniRatesAPI (https://unirateapi.com)'

# convert currencies
class conversionResults(BaseModel):
  amount: int | float
  from_: str
  result: int | float
  to: str

@app.get('/convert')
def convert(from_currency: str, to_currency: str, amount: int)-> conversionResults|tuple[str]:
    try:
        api_key = API_KEY
        result = convert_currency(api_key, from_currency, to_currency, amount)
        return conversionResults(
            amount=result["amount"],
            from_=result["from_"],
            result=result["result"],
            to=result["to"]
        )
    except Exception as e:
        return f"Error: {e}",

# get all currencies
@app.get('/currencies')
def fetch_currencies():
    try:
        api_key = API_KEY
        result = fetchCurrencies(api_key)
        return result
    except Exception as e:
        return [f"Error: {e}"]