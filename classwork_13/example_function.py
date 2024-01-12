def fahr_to_celsius(fahr_temp):
    print(f'Converting {fahr_temp} Fahr to Celsius')
    celsius_temp = (fahr_temp - 32) * 5 / 9
    return round(celsius_temp, 2)


print(fahr_to_celsius(42))
print(fahr_to_celsius(562))


def greet_user(username, is_first_login, days_since_last_login):
    if is_first_login:
        greeting = f'Welcome, {username}'
    else:
        greeting = f'Welcome back, {username}'
    if days_since_last_login > 0:
        greeting = f"{greeting}, you haven't been here for {days_since_last_login} days."
    print(greeting)
    return greeting


greet_user('Marius', True, 0)  # Welcome, Marius
greet_user('Marius2', False, 0)  # Welcome back, Marius
greet_user('Marius3', False, 2)  # Welcome back, Marius, you haven't been here for 2 days.

greet_user(
    days_since_last_login=10,
    username='Johnny',
    is_first_login=False,
)
