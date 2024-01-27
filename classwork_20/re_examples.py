import re

# Extract year, month, and day from a date string
pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
date_string = "2022-01-01, 2022-01-02, 2022-01-03"
matchs = pattern.findall(date_string)
for match in matchs:
    print(match)