from datetime import datetime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        if not self.is_valid_month(month):
            raise ValueError("Invalid month")
        self.month = int(month)
        self.day = int(day)

    def to_string(self):
        return f"{self.year}-{self.month}-{self.day}"

    @staticmethod
    def is_valid_month(month):
        if month < 1 or month > 12:
            return False
        return True

    @classmethod
    def make_from_string(cls, date_string):
        year, month, day = date_string.split("-")
        return cls(int(year), int(month), int(day))


date_obj = Date(2020, 12, 31)
print(date_obj.to_string())
other_date_obj = Date.make_from_string("2020-12-31")
print(other_date_obj)

print(Date.is_valid_month())
print(Date.is_valid_month())
