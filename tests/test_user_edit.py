from lib.my_requests import MyRequests
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


@allure.epic("Tests for edit feature")
class TestUserEdit(BaseCase):
    @allure.title("Successful edit for just created user")
    def test_edit_just_created_user(self):
        #Registration
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.asset_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        #Login
        login_data = {
            "email": email,
            "password": password
        }

        response2 = MyRequests.post("/user/login/", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #Edit
        new_name = "Changed Name"
        response3 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name})
        Assertions.asset_code_status(response3, 200)

        #Get
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name after edit")

    @allure.title("Unsuccessful edit user without authorization")
    def test_edit_without_auth(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.asset_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        user_id = self.get_json_value(response1, "id")

        #Edit
        new_name = "Changed Name"
        response2 = MyRequests.put(f"/user/{user_id}", data={"firstName": new_name})
        Assertions.asset_code_status(response2, 400)
        assert response2.content.decode("UTF-8") == "Auth token not supplied"

        #Get
        response3 = MyRequests.get(f"/user/{user_id}")
        Assertions.assert_json_value_by_name(response3, "username", first_name, "Wrong name after edit")

    @allure.title("Unsuccessful edit user with authorization as different user")
    def test_edit_just_created_user_as_another_user(self):
        #Register 1
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.asset_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        first_name = register_data["firstName"]
        user_id = self.get_json_value(response1, "id")

        #Register 2
        register_data = self.prepare_registration_data2()
        response2 = MyRequests.post("/user/", data=register_data)

        Assertions.asset_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        email1 = register_data["email"]
        password1 = register_data["password"]

        #Login
        login_data = {
            "email": {email1},
            "password": {password1}
        }

        response3 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        #Edit
        new_name = "Changed Name"
        response4 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid},
                                   data={"firstName": new_name})
        Assertions.asset_code_status(response4, 200)

        #Get
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "username", first_name, "Wrong name after edit")

    @allure.title("Unsuccessful edit user email to email without '@'")
    def test_edit_just_created_user_with_wrong_email(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.asset_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        #Login 
        login_data = {
            "email": email,
            "password": password
        }

        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #Edit
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        new_email = f"lernqa1{random_part}example1.com"
        response3 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid},
                                   data={"email": new_email})
        Assertions.asset_code_status(response3, 400)
        assert response3.content.decode("UTF-8") == "Invalid email format"

        #Get
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "email", email, "Wrong email after edit")

    @allure.title("Unsuccessful edit user name to too short name")
    def test_edit_just_created_user_with_short_name(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.asset_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        #Login
        login_data = {
            "email": email,
            "password": password
        }

        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #Edit
        short_name = "0"
        response3 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid},
                                   data={"firstName": short_name})
        Assertions.asset_code_status(response3, 400)
        assert response3.content.decode("UTF-8") == '{"error":"Too short value for field firstName"}'

        #Get
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", first_name, "Wrong firstName")