import requests 
import os
from datetime import date

import json
import pandas as pd

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv('API_KEY')

# ! You still want to add the name of the company. I think this is possible with the API, but in case it is not, you can use these files
# ? with open('lib/files/currency_pairs.json', 'r') as json_file:
# ?    currency_pairs = json.load(json_file)
# ? with open('lib/files/tickers.json', 'r') as json_file:
# ?    tickers = json.load(json_file)
  


def get_prices(date_from, tickers, date_to= date.today()):
  prices = {}
  for ticker in tickers:
    #parse response into a python dictionary
    response_prices = requests.get(f"https://eodhd.com/api/eod/{ticker}?fmt=json&from={date_from}&to={date_to}&period=d&order=a&api_token={API_KEY}").json()

    # remove unwanted keys with dict comprehnsion
    keys_to_remove = ['open', 'high', 'low', 'volume']
    prices[ticker]= [{key: value for key, value in response_price.items() if key not in keys_to_remove} for response_price in response_prices]
    print('getting prices...', ticker)

  # Convert the updated dictionary back to a JSON string
  return prices

def get_dividents(date_from, tickers, date_to= date.today()):
    dividents = {}

    for ticker in tickers:
      
      #parse response into a python dictionary
      response_dividents= requests.get(f"https://eodhd.com/api/eod/{ticker}?&from={date_from}&to={date_to}&period=d&fmt=json&api_token={API_KEY}").json()

      # remove unwanted keys with dict comprehnsion
      keys_to_remove = ['declarationDate', 'recordDate', 'currency', 'period']
      dividents[ticker] = [{key: value for key, value in response_divident.items() if key not in keys_to_remove} for response_divident in response_dividents]
      print('getting dividents...', ticker)

    # Convert the updated dictionary back to a JSON string
    return dividents

