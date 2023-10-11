import requests 


r = requests.get(f"https://eodhd.com/api/eod/AAPL.US?fmt=json&&api_token=${API_key}")


print(r.json())