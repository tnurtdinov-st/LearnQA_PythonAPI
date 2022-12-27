import allure
import requests
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase


@allure.epic("Тесты на Delete")
@allure.feature("Deleting")
class TestUserDelete(BaseCase):
    @allure.title("Попытка удалить пользователя по ID 2")
    @allure.story("Удаление пользователя с id=2")
    def test_delete_user_with_id_2(self):

        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        # LOGIN
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # DELETE
        response2 = requests.delete("https://playground.learnqa.ru/api/user/2", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.asset_code_status(response2, 400)
        assert response2.content.decode("UTF-8") == 'Please, do not delete test users with ID 1, 2, 3, 4 or 5.'

        # ASSERTING
        response3 = requests.get("https://playground.learnqa.ru/api/user/2", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.asset_code_status(response3, 200)
        assert response3.content.decode(
            "UTF-8") == '{"id":"2","username":"Vitaliy","email":"vinkotov@example.com","firstName":"Vitalii","lastName":"Kotov"}'

    @allure.title("Успешное удаление пользователя")
    @allure.description("Создать пользователя, авторизоваться из-под него, удалить, затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.")
    def test_delete_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.asset_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response2 = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.asset_code_status(response2, 200)

        # ASSERTING
        response3 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.asset_code_status(response3, 404)
        assert response3.content.decode("UTF-8") == 'User not found'

    @allure.title("Неуспешное удаление пользователя")
    @allure.description("Попробовать удалить пользователя, будучи авторизованными другим пользователем.")
    def test_delete_user_from_different_user(self):
        # REGISTER 1
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.asset_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        user_id = self.get_json_value(response1, "id")

        # REGISTER 2
        register_data = self.prepare_registration_data2()
        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.asset_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email1 = register_data["email"]
        password1 = register_data["password"]

        # LOGIN
        login_data = {
            "email": {email1},
            "password": {password1}
        }

        response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # DELETE
        response4 = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.asset_code_status(response4, 200)

        # ASSERTING
        response5 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        Assertions.asset_code_status(response5, 200)
        assert response5.content.decode("UTF-8") == '{"username":"' + first_name + '"}'