import requests
import pytest

class TestFirstApi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/ajax/api/homework_cookie"
        response = requests.get(url, verify=False)
        print(response.text)
        cookie = response.cookies
        print(cookie)
        assert response.status_code == 200, "Status code is incorrect"
