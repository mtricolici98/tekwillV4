from collections import namedtuple

user = ('172717', '1123', 1998)

print(user[0])
print(user[1])
print(user[2])

UserTuple = namedtuple('User', ['name', 'password', 'birth_year'])

user = UserTuple('172717', '1123', 1998)

print(user[0])
print(user[1])
#
print(user.name)
print(user.password)
print(user.birth_year)

user = {
    'name': "123123",
    'password': "<PASSWORD>"
}

date = "172712, 1123, 1998;1727417, 1123, 1998;17123122717, 1123, 1998"
list_of_users = []
for el in date.split(';'):
    usr_data = el.split(', ')
    list_of_users.append(
        (usr_data[0], usr_data[1], usr_data[2])
    )

print(list_of_users)
for user in list_of_users:
    print(user[0])
    print(user[1])
    print(user[2])

date = "172712, 1123, 1998;1727417, 1123, 1998;17123122717, 1123, 1998"
list_of_users = []
for el in date.split(';'):
    list_of_users.append(UserTuple(*el.split(', ')))

print(list_of_users)
for user in list_of_users:
    print(user.name)

[1, 2, 3, 4, 5]


