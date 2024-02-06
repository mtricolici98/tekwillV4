from datetime import datetime


class Human:

    def __init__(self, name):
        self.name = name

    def get_full_name(self):
        return self.name

    def get_age(self, date_of_brith):
        date_of_birth = datetime.strptime(date_of_brith, "%d/%m/%Y").date()
        return datetime.now().year - date_of_birth.year

    def __str__(self):
        return self.name


a = Human('Marius')
a.get_age(input('DOB'))

str(a)