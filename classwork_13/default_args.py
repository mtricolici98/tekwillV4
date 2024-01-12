def greet_user(username, is_first_login=False, days_since_last_login=0):
    if is_first_login:
        greeting = f'Welcome, {username}'
    else:
        greeting = f'Welcome back, {username}'
    if days_since_last_login > 0:
        greeting = f"{greeting}, you haven't been here for {days_since_last_login} days."
    print(greeting)
    return greeting


greet_user('Marius')  # Welcome back, Marius
greet_user('Marius1', True)  # Welcome, Marius
greet_user('Marius2', False, 13)  # Welcome, Marius, you haven't been here for 13 days.


def print_list(my_list, symbol='|'):
    for element in my_list:
        print(symbol, element, symbol)


print_list([1, 2, 3, 4], "+")
print_list([1, 2, 3, 4])
