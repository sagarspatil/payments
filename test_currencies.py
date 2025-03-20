import requests
import json

url = "https://api.stealthex.io/v4/currencies"

headers = {"Authorization": "Bearer bd658a48-6bd7-4f7a-af85-f5dcec47516b"}

response = requests.get(url, headers=headers)

with open('currencies.json', 'w') as f:
    json.dump(response.json(), f, indent=2)
