import string

LIST_OF_COMMON_PASSWORD = ['Admin1!', 'Admin2!', 'Admin3!']

def password_check(pwd):
    if pwd in LIST_OF_COMMON_PASSWORD:
        return False
    has_upper = any(char.isupper() for char in pwd)
    has_lower = any(char.islower() for char in pwd)
    has_digits = any(char.isdigit() for char in pwd)
    has_special_character = any(char in string.punctuation for char in pwd)
    has_length = len(pwd) >= 8
    print(has_upper, has_lower, has_digits, has_special_character, has_length)
    return has_upper and has_lower and has_digits and has_special_character and has_length


if __name__ == '__main__':
    password = input('Enter your password: ')
    if password_check(password):
        print("Password is good")
    else:
        print("Password is not good")
