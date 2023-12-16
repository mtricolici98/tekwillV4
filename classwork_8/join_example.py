my_list = ['Marius', 'Ion', 'Nelly']
print(my_list)

reprezentare = "; ".join(my_list)
print(reprezentare)

reprezentare = " ".join(my_list)
print(reprezentare)

reprezentare = "".join(my_list)
print(reprezentare)

csv = 'marius,ion,nelly'  # comma separated values
lista_de_participanti = csv.split(',')
print(lista_de_participanti)
lista_de_participanti.append('vitalie')
new_csv = ','.join(lista_de_participanti)
print(new_csv)

list_de_numbere = [5, 4, 3, 5, 7]
list_de_Str = []

for el in sorted(list_de_numbere):
    list_de_Str.append(str(el))

print(','.join(list_de_Str))
