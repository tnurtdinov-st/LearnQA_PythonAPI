import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/ajax/api/login", data = data, verify = False)

        assert "auth_sid" in response1.cookies, "There is no auth cookie in the responce"
        assert "x-csrf-token" in response1.headers, ""