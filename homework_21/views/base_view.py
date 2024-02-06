import abc


class BaseView(abc.ABC):

    @abc.abstractmethod
    def show(self, user_info) -> bool:
        pass
