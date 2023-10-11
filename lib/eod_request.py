import requests 
import os
from dotenv import ( load_dotenv, dotenv_values )

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv('API_KEY')

r = requests.get(f"https://eodhd.com/api/exchanges-list/?api_token={API_KEY}")


print(r.json())