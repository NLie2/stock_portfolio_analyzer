import requests 

API_key = "63aef4c401d202.68341572"

r = requests.get(f"https://eodhd.com/api/eod/AAPL.US?fmt=json&&api_token=demo")


print(r.json())