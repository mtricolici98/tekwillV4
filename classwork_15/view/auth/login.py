from classwork_15.controller.auth import authenticate_user
from classwork_15.view.input_helpers import get_email_input, get_password_input


def login_view():
    email_input = get_email_input()
    attemt_limit = 3
    current_attempts = 0
    try:
        while True:
            if attemt_limit > 0 and current_attempts >= attemt_limit:
                raise Exception("Too many attempts")
            password = get_password_input()
            result = authenticate_user(email_input, password)
            if result:
                print("Logged in successfully")
                return True
            else:
                print('Invalid password')
            current_attempts += 1
    except Exception as ex:
        print(ex)
        print('Login failed')
