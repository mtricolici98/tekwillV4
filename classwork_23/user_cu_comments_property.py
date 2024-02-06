class Comment:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._comments = []
        self._posts = []
        self._likes = []
        self.is_banned = False

    @property
    def comments(self):
        if self.is_banned:
            return []
        if not self._comments:
            self._load_comments()
        return self._comments

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def post(self):
        if self.is_banned:
            return []
        if not self._posts:
            self._load_posts()
        return self._posts

    def get_username(self):
        return self.name

    def _load_comments(self):
        print("loading comments")  # Un oarecare lucru
        self._comments = [Comment("Hello")]

    def _load_posts(self):
        print("loading posts")  # Un oarecare lucru
        self._comments = []


user = User("Marius", "Tr")

print(user.full_name)

print(user.comments)
print(user.comments)
print(user.comments)
