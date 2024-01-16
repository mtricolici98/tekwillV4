from classwork_15.controller.auth import register_user, RegistrationError, DatabaseError
from classwork_15.view.input_helpers import get_email_input, get_password_input


def register_view():
    email_input = get_email_input()
    password = get_password_input(True)
    try:
        register_user(email_input, password)
        print('Registration successful')
    except RegistrationError as ex:
        print(f"Registration Failed: {ex}")
    except DatabaseError as ex:
        print(f"{ex}, please contact administrator")
