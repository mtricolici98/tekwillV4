import abc


class SignInRequest(abc.ABC):

    def get_expiration_date(self):
        return 14  # Days

    def website_singing_in(self):
        return "medium"

    @abc.abstractmethod
    def login(self, data) -> bool:
        pass



class FacebookSignInRequest(SignInRequest):

    def login(self, data):
        print(f"Doing facebook login on {self.website_singing_in()} with expiration date of login being",
              self.get_expiration_date())


class TwitterSignInRequest(SignInRequest):

    def login(self, data):
        print(f"Doing twitter login on {self.website_singing_in()} with expiration date of login being",
              self.get_expiration_date())


class GitHubSignInRequest(SignInRequest):

    def login(self, data):
        print(f"Doing github login on {self.website_singing_in()} with expiration date of login being",
              self.get_expiration_date())



TwitterSignInRequest().login([])
FacebookSignInRequest().login([])

a = GitHubSignInRequest()

print(isinstance(a, GitHubSignInRequest))
print(isinstance(a, SignInRequest))

print(isinstance(a, TwitterSignInRequest))

