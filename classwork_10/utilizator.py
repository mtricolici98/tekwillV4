user = {}
nume_utilizator = input("Username")
parola = input("Password")

user["username"] = nume_utilizator
print(user)
user["password"] = parola
print(user)

new_password = input("Password")
user["password"] = new_password
print(user)

for key in user:
    print(f"Cheia: {key} contine valoare {user[key]}")


