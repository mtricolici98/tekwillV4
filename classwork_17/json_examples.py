import json

json_string = '[1,2,3]'

print(type(json_string))

data = json.loads(json_string)

print(type(data))
print(data)

with open('mdl.json', 'r') as file:
    # json_string = file.read()
    # currency_data = json.loads(json_string)
    currency_data = json.load(file)

print(type(currency_data))
print(currency_data)

suma_dolari = int(input('Suma in dolari'))

suma_lei = suma_dolari * currency_data['usd']['inverseRate']
print(f"{suma_dolari} in lei este: {suma_lei:.2f}")
