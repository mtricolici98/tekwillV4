class Comment:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text


class User:

    def __init__(self, name):
        self.name = name
        self._comments = []
        self._posts = []
        self._likes = []
        # self._load_comments()

    def __getattr__(self, item):
        if item == 'comments':
            if not self._comments:
                self._load_comments()
            return self._comments
        if item == 'comments':
            if not self._posts:
                self._load_comments()
            return self._posts
        if item == 'comments':
            if not self._comments:
                self._load_comments()
            return self._comments
        return self.__getattr__(item)

    def _load_comments(self):
        print("loading comments")  # Un oarecare lucru
        self._comments = [Comment("Hello")]


user = User("Marius")
# print(user.comments)
# print(user.comments)
# print(user.comments)
