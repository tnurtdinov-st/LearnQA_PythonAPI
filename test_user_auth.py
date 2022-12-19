import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data = data, verify = False)
        print(response1.headers)
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token in the response"
        assert "user_id" in response1.json(), "There is no user id in the response"
        print(response1.json())
        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_auth = response1.json()["user_id"]

        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": token}, cookies = {"auth_sid": auth_sid}, verify = False)
        assert "user_id" in response2.json(), "There is no user id in the 2 response"
        print(response2.json())
        user_id_check = response2.json()["user_id"]
        assert user_id_auth == user_id_check, "User id from auth method is not equal to user from check method"