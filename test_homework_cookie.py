import requests
import pytest

class TestFirstApi:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/ajax/api/homework_cookie"
        response = requests.get(url, verify=False)
        print(response.text)
        cookie = response.cookies
        print(cookie)
        assert response.status_code == 200, "Status code is incorrect"
        #В https://playground.learnqa.ru/ajax/api/homework_cookie нет auth_sid или чего то еще, за что можно было бы цепляться, оставил пока только проверку на статус код и на HomeWork из ответа
        assert "HomeWork" in response.cookies, "There is no HomeWork cookie in the responce"
