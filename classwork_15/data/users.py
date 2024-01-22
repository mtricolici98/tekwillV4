# {'email': str, 'password': str}
import json
import os


def get_users_table() -> list:
    if os.path.exists('users.json') and os.path.isfile('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return []


def save_user_table(user_data: list):
    with open('users.json', 'w') as file:
        return json.dump(user_data, file)
