def get_username():
    return input('Username: ')


def greet_user():
    username = get_username()
    print(f"Salut, {username}")


def greet_n_users():
    for n in range(int(input())):
        greet_user()


#
# greet_user()
#
# greet_n_users()

#
#
#

def some_function():
    pass
    print('12031203')


some_function()

print(max(4, 3, 12))


def my_max(nr1, nr2):
    if nr1 > nr2:
        print(nr1)
    else:
        print(nr2)


my_max(10, 50)
result = my_max(62, 50)

print(result)


