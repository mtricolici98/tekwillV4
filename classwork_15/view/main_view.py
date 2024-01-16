from classwork_15.controller.auth import log_out, get_current_user, get_is_admin, get_all_users
from classwork_15.view.auth.login import login_view
from classwork_15.view.auth.registration import register_view
from classwork_15.view.input_helpers import get_strict_number_view


def main_menu_unauthorized():
    print('1: Register')
    print('2: Login')
    print('0: Quit')
    choice = get_strict_number_view()
    match choice:
        case 0:
            exit()
        case 1:
            register_view()
        case 2:
            login_view()


def list_all_users():
    for user in get_all_users():
        print(user)


def menu_authorized():
    print(f'Your are logged in as {get_current_user()}')
    print('0. Log-out')
    if get_is_admin():
        print('99. Show all users')
    choice = get_strict_number_view()
    match choice:
        case 99:
            if get_is_admin():
                list_all_users()
        case 0:
            log_out()


def main():
    while True:
        active_user = get_current_user()
        if active_user:
            menu_authorized()
        else:
            main_menu_unauthorized()
