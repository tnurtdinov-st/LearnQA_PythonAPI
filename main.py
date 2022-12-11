from json.decoder import JSONDecodeError
import requests
import json

payload={"name": "User"}
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not in json format")