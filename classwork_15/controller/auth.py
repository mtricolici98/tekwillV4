import hashlib
import json
import os.path

from classwork_15.data.users import get_users_table, save_user_table

current_user = None
is_admin = False

ADMIN_EMAIL = 'admin@admin.local'
ADMIN_PASSWORD = '123'

if os.path.exists('current_user.json'):
    current_user = json.load(open('current_user.json'))


class RegistrationError(Exception):
    pass


class LoginError(Exception):
    pass


class DatabaseError(Exception):
    pass


def save_current_user():
    json.dump(current_user, open('current_user.json', 'w'))


def authenticate_user(email, password):
    global current_user
    global is_admin
    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        current_user = email
        is_admin = True
        return True

    for user in get_users_table():
        if user['email'] == email:
            if user['password'] != pass_hash(password):
                raise LoginError('Incorrect password')
            current_user = email
            save_current_user()
            return True

    raise LoginError("Incorrect email")


def pass_hash(text: str):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def register_user(email, password):
    user_data = get_users_table()
    all_registered_emails = [a['email'] for a in user_data]
    if len(user_data) >= 2:
        raise DatabaseError('Database full')
    if email in all_registered_emails:
        raise RegistrationError('Email already registered')
    pass_hash(password)
    user_data.append(
        {'email': email, 'password': pass_hash(password)}
    )
    save_user_table(user_data)
    return True


def log_out():
    global current_user
    global is_admin
    current_user = None
    save_current_user()
    is_admin = False


def get_current_user():
    return current_user


def get_is_admin():
    return is_admin


def get_all_users():
    return get_users_table()
