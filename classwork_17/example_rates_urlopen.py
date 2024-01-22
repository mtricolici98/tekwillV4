import json
import os.path
from urllib.request import urlopen

my_data = urlopen('https://www.floatrates.com/daily/mdl.json')
json_data = my_data.read().decode('utf-8')
print(json_data)

currency_data = json.loads(json_data)

suma_dolari = int(input('Suma in dolari'))

suma_lei = suma_dolari * currency_data['usd']['inverseRate']
data = currency_data['usd']['date']
print(f"{suma_dolari} in lei este: {suma_lei:.2f} la data de {data}")

if not os.path.exists(os.path.join(os.getcwd(), 'history.json')):
    json.dump([], open('history.json', 'w'))

history = json.load(open('history.json'))  # Va fi o lista
history.append(
    {'suma_lei': suma_lei,
     'suma_dolari': suma_dolari}
)
json.dump(history, open('history.json', 'w'))
