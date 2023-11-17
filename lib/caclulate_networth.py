import pandas as pd
import json 

# ! write a functon that converts prices into euro 
# BONUS: MAKE IT DYNAMIC SO THE APP CAN BE USED BY PEOPLE WITH DIFFERENT PREFERRED CURRENCIES

#Get  ticker name pairs
with open('lib/files/ticker_by_symbol.json', 'r') as json_file:
    ticker_name_pairs = json.load(json_file)
  

def calculate_eur_values(row):
    #converts one row to euro 
    close = row['close']
    adjusted_close = row['adjusted_close']
    fx_close = row['close']

    if pd.notna(fx_close):
        close_eur = close / fx_close / 100 if 'GBP' in row['currencyPair'] else close / fx_close
        adjusted_close_eur = adjusted_close / fx_close / 100 if 'GBP' in row['currencyPair'] else adjusted_close / fx_close
    else:
        close_eur = close / 100 if 'GBP' in row['currencyPair'] else close
        adjusted_close_eur = adjusted_close / 100 if 'GBP' in row['currencyPair'] else adjusted_close

    return pd.Series({
        'date': row['date'],
        'close_eur': close_eur,
        'adjusted_close_eur': adjusted_close_eur,
        'name': row['name']
    })

def convertToEuro(trades, prices ):
  # Get TickerCurrency pairs
  
  # Create a list to store the TickersCurrencyPair objects
  TickersCurrencyPairs = []

  # Iterate through the prices list to generate TickersCurrencyPair
  ticker_set = set()  # Used to keep track of unique tickers
  for trade in trades:
      ticker = trade["ticker"]
      if ticker not in ticker_set:
          # Only add the Ticker and CurrencyPair once per unique Ticker
          ticker_set.add(ticker)
          TickersCurrencyPairs.append({
              "ticker": trade["ticker"],
              "currencyPair": trade["currencyPair"],
              "name": ticker_name_pairs[ticker]
          })
  
  prices_eur = prices.copy()

  # merge currency pair from trade to the prices_eur table
  for ticker_currency_pair in TickersCurrencyPairs: 
    ticker = ticker_currency_pair['ticker']
    name = ticker_currency_pair['name']

    for price in prices_eur[ticker]: 
      price['currencyPair'] = ticker_currency_pair['currencyPair']

      # Convert each row to euro 
      price['date', 'close_eur', 'adjusted_close_eur', 'Name'] = calculate_eur_values(price)
  # input: prices table
  # output: prices table in euro 

  return prices_eur

# ! write a function to add missing dates into price table 
def addMissingDates():
  # input: prices table
  # output: prices table without missing dates 

  pass

# ! write a function to calculate the networth table 
def get_networth(): 
  # input: prices table without missing dates, and all in one currency
  # output: networth table 

  # on every day, how many pieces of this stock did you have. 
  # on  every day how much were my earnings worth (cum shares * value)

  # portfolio worth: add up all worths for all stocks per day 

  # If a stock was sold on that day, it does not appear in the networth of that day. 
  # Use unadjusted close

  pass

