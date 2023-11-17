import pandas as pd
import json 

from datetime import datetime, timedelta

# ! write a functon that converts prices into euro 
# BONUS: MAKE IT DYNAMIC SO THE APP CAN BE USED BY PEOPLE WITH DIFFERENT PREFERRED CURRENCIES

#Get  ticker name pairs
with open('lib/files/ticker_by_symbol.json', 'r') as json_file:
    ticker_name_pairs = json.load(json_file)
  

def calculate_eur_values(row, exchange_rate, close = 'close'):
    #converts one row to euro 
    #if you prefer using adjusted close call function with close='adjusted_close'
    
    price_eur = row['close'] / exchange_rate[row['date']][close]

    return price_eur 

# ! write a function to add missing dates into price table 
def addMissingDates(prices_table):
  # input: prices table
  # output: prices table without missing dates 
    # merge currency pair from trade to the prices_eur table
  prices_by_date = {}
  return prices_by_date

  # for company in prices_table: 
  #   for price in company: 
  #     date = datetime.strptime(price['date'], '%Y-%m-%d')
  #     print(date)
  #     prices_by_date[prices_eur['date']] = {'ticker': ticker, 'price_eur': exchangedprice}
      

  #     date = datetime.strptime(price['date'], '%Y-%m-%d')
  #     print(date)
  #     if date_temp != 0: 
  #       time_difference = date - date_temp
  #       days_difference = time_difference.days
  #       if days_difference > 1: 
  #         for i in range(1, days_difference):
  #           missing_date = date_temp + timedelta(days=i)
  #           print('missing',  missing_date)
  #           # Create a new object with the missing date
  #           new_price = {'date': missing_date.strftime('%Y-%m-%d'), 'price_eur': price['price_eur'] }
  #           # print(new_price)
  #         # insert rows that are a copy of the earliest available row, but with thte missing dates
  #     date_temp = datetime.strptime(price['date'], '%Y-%m-%d')

  # for prices_for_company in prices_table: 
  #   print(prices_for_company)
  #   check_consecutive_dates

def check_consecutive_dates(date_strings, max_gap=1):
    # Convert string dates to datetime objects
    date_objects = [datetime.strptime(date_str, '%Y-%m-%d') for date_str in date_strings]

    # Check the differences between consecutive dates
    for i in range(1, len(date_objects)):
        time_difference = date_objects[i] - date_objects[i - 1]
        days_difference = time_difference.days

        if days_difference > max_gap:
            # Perform a certain action when the gap is more than one day
            print(f"Non-consecutive dates found: {date_objects[i - 1].strftime('%Y-%m-%d')} and {date_objects[i].strftime('%Y-%m-%d')}")
            # returns the index of the row and how many times it needs to be replicated
            return( i-1, days_difference)

def convertToEuro(trades, prices, exchange_rates ):
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
      if price['currencyPair'] != '-': 
        exchange_rate_currencyPair = exchange_rates[price['currencyPair']]

        # Convert each row to euro 
        exchangedprice = calculate_eur_values(price, exchange_rate_currencyPair)

        price['price_eur'] = exchangedprice
      


  return prices_eur



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

