import math
from datetime import datetime


class Human:

    def __init__(self, first, last, dob):
        self.first = first
        self.last = last
        self.dob = dob

    def __str__(self):
        return f"{self.get_full_name()}: age {self.get_age()}"

    def get_age(self):
        td = datetime.now() - self.dob
        return td.days // 365

    def get_full_name(self):
        return f"{self.first} {self.last}"


if __name__ == '__main__':
    marius = Human('Marius', 'Tr', datetime(1998, 1, 30))
    print(marius)
