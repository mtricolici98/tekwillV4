import json


class UserDataBase:

    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename) as f:
                self.data = json.load(f)
        except Exception:
            self.data = []

    def save_to_file(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f)
        except Exception:
            print("Failed to save data")

    def add_data(self, name, email, password):
        user = {
            'name': name,
            'email': email,
            'password': password
        }
        self.data.append(user)
        self.save_to_file()


if __name__ == '__main__':
    database = UserDataBase('user_data.json')

    print(database.data)
    # database.add_data(input(), input(), input())
    # print(database.data)
    a = 1
    my_string = ""
    my_set = set()
