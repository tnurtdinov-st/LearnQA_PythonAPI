import requests
import pytest

class TestFirstApi:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/ajax/api/homework_header"
        response = requests.get(url, verify=False)
        print(response.text)
        print(response.headers)
        assert response.status_code == 200, "Status code is incorrect"
