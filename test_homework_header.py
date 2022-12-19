import requests
import pytest

class TestFirstApi:
    def test_homework_cookie(self):
        url = "https://playground.learnqa.ru/ajax/api/homework_header"
        response = requests.get(url, verify=False)
        print(response.headers)
        response.headers.get("x-secret-homework-header")
        assert "x-secret-homework-header" in response.headers, "There is no x-secret-homework-header token in the response"
        assert "Some secret value" in response.headers.get("x-secret-homework-header"), "There is incorrect value in the response"

