import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAuth(BaseCase):

    exclude_params = [("no_cookie"), ("no_token") ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data, verify=False)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_auth = self.get_json_value(response1, "user_id")

        assert "user_id" in response1.json(), "There is no user id in the response"
        print(response1.json())
        self.user_id_auth = response1.json()["user_id"]

    def test_auth_user(self):
        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": self.token}, cookies = {"auth_sid": self.auth_sid}, verify = False)
        Assertions.assert_json_value_by_name(response2, "user_id", self.user_id_auth, error_message="User id from auth method is not equal to user id from check method")

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={"x-csrf-token": self.token}, verify = False)
        else:
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", cookies = {"auth_sid": self.auth_sid}, verify = False)

        Assertions.assert_json_value_by_name(response2,"user_id", 0, f"User is authorized with condition {condition}")
