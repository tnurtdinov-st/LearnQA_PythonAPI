from json.decoder import JSONDecodeError
import requests
import json

response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_auth_cookie",
                         data={"login": "secret_login", "password": "secret_pass"})
cookie_value = response1.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})
response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies = cookies)
print(response2.text)





