import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("apiKey")
if not API_KEY:
    print("API key not set!")
    exit(1)

url = "https://api.stealthex.io/v4/currencies?limit=1"
headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}

r = requests.get(url, headers=headers)
if r.status_code == 200:
    print("API key is working!")
else:
    print("API key test failed:", r.status_code, r.text)
