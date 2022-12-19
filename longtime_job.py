import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", verify=False)
token = response.json()['token']
t = response.json()['seconds']
print("Token: " + token + " Time: " + str(t))

while True:
    response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token}, verify=False)
    if "Job is NOT ready" in response.json()['status']:
        print("Status: " + response.json()['status'])
        time.sleep(int(t))
    elif "Job is ready" in response.json()['status']:
        print("Status: " + response.json()['status'])
        print("Result: " + response.json()['result'])
        break