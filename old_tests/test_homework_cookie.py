import requests
import pytest

class TestFirstApi:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/ajax/api/homework_cookie"
        response = requests.get(url, verify=False)
        cookie = response.cookies
        print(cookie)
        #Этого достаточно?
        assert "HomeWork" in response.cookies, "There is no HomeWork cookie in the response"
