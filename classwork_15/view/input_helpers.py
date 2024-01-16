from classwork_15.controller.helpers import is_valid_email


def get_input_or_stop_view():
    optiune = input('Alege produsul sau scrie stop: ')
    if optiune.lower() == 'stop':
        return True, None
    return False, optiune


def get_strict_number_view(message="Intordu un numar: "):
    while True:
        try:
            print()
            value = int(input(message))
            print()
            return value
        except ValueError:
            print('Se cere o valoare numerica')


def check_password_strength(password):
    if (len(password) >= 8 and
            any(a.isupper() for a in password) and
            any(b.lower() for b in password) and
            any(c.isdigit() for c in password) and
            any(c.isalpha() for c in password)
    ):
        return True
    return False


def get_email_input():
    while True:
        email_input = input('Enter your email')
        if is_valid_email(email_input):
            return email_input
        else:
            print('Invalid email input')


def get_password_input(check_strength=False):
    current_attempts = 0
    while True:
        password = input('Enter your password:')
        if not check_strength:
            return password
        if check_password_strength(password):
            return password
        else:
            print('Password did not match strength criteria')
            current_attempts += 1
