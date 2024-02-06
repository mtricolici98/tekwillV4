from homework_21.views.base_view import BaseView
from homework_21.views.login_view import LoginView


class RegisterView(BaseView):

    def show(self):
        print("hello")


def show_view(view_to_show: BaseView):
    view_to_show.show()


def main():
    user = None
    if not user:
        show_view(LoginView())
    show_view(RegisterView())


if __name__ == '__main__':
    main()
