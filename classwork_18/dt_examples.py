from datetime import datetime, timedelta
import pytz
from dateutil.relativedelta import relativedelta

chisinau_tz = pytz.timezone('Europe/Chisinau')

data_azi = datetime(
    2024,
    1,
    23,
    18,
    55,
    tzinfo=chisinau_tz
)

data_maine = datetime(
    2024,
    1,
    24,
    19,
    0,
    tzinfo=chisinau_tz
)

print(data_azi)

print(data_azi.day)
print(data_azi.year)

acum = datetime.now(chisinau_tz)
print(acum)

print(data_azi > acum)
print(data_maine > acum)

print(data_maine - data_azi)

a = timedelta(seconds=100000)
print(a)

rd = relativedelta(years=10)
print(datetime.now() + rd)