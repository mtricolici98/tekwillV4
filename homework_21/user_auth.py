import json


class ClassicAuth:

    def __init__(self, know_user_password: dict):
        self.know_user_password = know_user_password

    def register(self, username, password):
        if username in self.know_user_password:
            raise ValueError("User already exists")
        self.know_user_password[username] = password


class StrongPasswordAuth(ClassicAuth):

    def _check_password(self, password):
        if (len(password) >= 8 and
                any(a.isupper() for a in password) and
                any(b.lower() for b in password) and
                any(c.isdigit() for c in password) and
                any(c.isalpha() for c in password)):
            return True
        return False

    def register(self, username, password):
        if self._check_password(password):
            super().register(username, password)
        else:
            raise ValueError("Password is too weak")


class DatabaseAuth(ClassicAuth):

    def __init__(self, database_file_path):
        self.db_file_path = database_file_path
        self.user_data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.db_file_path) as f:
                self.user_data = json.load(f)
        except Exception:
            self.user_data = {}

    def save_to_file(self):
        try:
            with open(self.db_file_path, 'w') as f:
                json.dump(self.user_data, f)
        except Exception:
            print("Failed to save data")

    def register(self, username, password):
        self.user_data[username] = password
        self.save_to_file()


auth_object = ClassicAuth({"admin": "<PASSWORD>"})

auth_object.register("admin1", "<PASSWORD>")

auth_object = StrongPasswordAuth({"admin": "<PASSWORD>"})

auth_object.register("admin1", "<PASSWORd1>")

auth_object = DatabaseAuth("user_data.json")

auth_object.register("admin1", "<PASSWORd1>")
