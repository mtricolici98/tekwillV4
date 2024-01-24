import json

from datetime import datetime

date_now = datetime.now()

user = {
    'username': "Marius",
    'date_of_birth': date_now
}

print(user)

with open('user.json', 'w') as file:
    user['date_of_birth'] = user['date_of_birth'].strftime("%d/%m/%Y")
    json.dump(user, file)
