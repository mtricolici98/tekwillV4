from datetime import datetime, timedelta

string_time = input()

actual_datetime = datetime.strptime(string_time, '%d/%m/%Y %H:%M')

print(actual_datetime)

# Parse is a better automatic alternative
from dateutil.parser import parse

parsed = parse("10/12/2020 10:00:13")
print(parsed)

from dateutil.relativedelta import relativedelta

info = relativedelta(datetime.now(), datetime.now() + timedelta(100))
print(info)

