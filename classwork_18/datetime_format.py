from datetime import datetime

import pytz

chisinau_tz = pytz.timezone('Europe/Chisinau')

now = datetime.now(chisinau_tz)

print(now)

print(now.strftime("%d %m %H:%M"))
print(now.strftime("%d/%m/%Y %H:%M"))
print(now.strftime("%d/%m/%y %H:%M %z"))


# print(now.strftime("%D"))