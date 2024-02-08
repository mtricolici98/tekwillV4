import json

import pandas
import requests

response = requests.get('https://www.floatrates.com/daily/mdl.json')

json_data = response.json()
print(json_data)

data = pandas.read_json(json.dumps(json_data))
print(data)
data.transpose()
print(data)
# data['rate'].plot(kind='bar')
data.to_excel("output.xlsx")
