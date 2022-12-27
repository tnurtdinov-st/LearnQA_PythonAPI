from lib.my_requests import MyRequests
import pytest
import string
import random
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):

    def test_create_user_succsessfuly(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.asset_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data = data)

        Assertions.asset_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_incorrect_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        print(response.text)
        Assertions.asset_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", f"Unexpected response content {response.content}"

    random_part = datetime.now().strftime("%m%d%Y%H%M%S")
    data = [
        {'username': 'lernqa',
         'firstName': 'lernqa',
         'lastName': 'lernqa',
         'email': f"lernqa{random_part}@example.com"},
        {'password': '123',
         'firstName': 'lernqa',
         'lastName': 'lernqa',
         'email': f"lernqa{random_part}@example.com"},
        {'password': '123',
         'username': 'lernqa',
         'lastName': 'lernqa',
         'email': f"lernqa{random_part}@example.com"},
        {'password': '123',
         'username': 'lernqa',
         'firstName': 'lernqa',
         'email': f"lernqa{random_part}@example.com"},
        {'password': '123',
         'username': 'lernqa',
         'firstName': 'lernqa',
         'lastName': 'lernqa'}
    ]

    @pytest.mark.parametrize('data', data)
    def test_create_without_filed(self, data):
        response = MyRequests.post("/user/", data=data)
        Assertions.asset_code_status(response, 400)
        if "password" not in data:
            assert response.content.decode("UTF-8") == "The following required params are missed: password"
        elif "username" not in data:
            assert response.content.decode("UTF-8") == "The following required params are missed: username"
        elif "firstName" not in data:
            assert response.content.decode("UTF-8") == "The following required params are missed: firstName"
        elif "lastName" not in data:
            assert response.content.decode("UTF-8") == "The following required params are missed: lastName"
        elif "email" not in data:
            assert response.content.decode("UTF-8") == "The following required params are missed: email"

    def test_create_user_with_short_name(self):
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        data = {
            'password': '123',
            'username': 'l',
            'firstName': 'lernqa',
            'lastName': 'lernqa',
            'email': f"lernqa{random_part}@example.com"
        }
        response = MyRequests.post("/user/", data=data)
        Assertions.asset_code_status(response, 400)
        assert response.content.decode("UTF-8") == "The value of 'username' field is too short"

    def test_create_user_with_long_name(self):
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(251))
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        data = {
            'password': '123',
            'username': name,
            'firstName': 'lernqa',
            'lastName': 'lernqa',
            'email': f"lernqa{random_part}@example.com"
        }
        response = MyRequests.post("/user/", data=data)
        Assertions.asset_code_status(response, 400)
        assert response.content.decode("UTF-8") == "The value of 'username' field is too long"
