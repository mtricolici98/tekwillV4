password = input('pass')
contains_numbers = password.isalnum() and not password.isalpha()

lower_no_numbers = password.islower() and not contains_numbers
upper_no_numbers = password.isupper() and not contains_numbers
only_numbers = password.isnumeric()

if len(password) < 8 or only_numbers or upper_no_numbers or lower_no_numbers:
    print("password is weak")
else:
    mari_mici = not password.isupper() and not password.islower()
    if contains_numbers and mari_mici:
        print(f"Is strong")
    else:
        print('Is good')
