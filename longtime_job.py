import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()['token']
print("Token: " + token)

while True:
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
    if "Job is NOT ready" in response.json()['status']:
        print("Status: " + response.json()['status'])
        time.sleep(20)
    elif "Job is ready" in response.json()['status']:
        print("Status: " + response.json()['status'])
        print("Result: " + response.json()['result'])
        break