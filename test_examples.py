import requests
import pytest




url = "https://playground.learnqa.ru/ajax/api/homework_cookie"

response = requests.get(url, verify=False)
print(response.text)
print("1")
print(response.cookies)


