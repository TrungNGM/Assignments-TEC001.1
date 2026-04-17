import requests
import json

request = "http://127.0.0.1:5000/airport/EFHK"
response = requests.get(request).json()
print(response)