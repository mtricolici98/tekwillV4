import os

lista_de_fisiere = os.listdir(os.getcwd())
print(lista_de_fisiere)

print(os.path.getsize('config.json'))

lista_de_timpuri = list(map(os.path.getsize, lista_de_fisiere))
print(lista_de_timpuri)

lista_de_fisiere_sortata = sorted(lista_de_fisiere, key=os.path.getsize)
print('---------------')
print(lista_de_fisiere_sortata)

lista_de_fisiere_sortata = sorted(lista_de_fisiere, key=os.path.getmtime)
print('---------------')
print(lista_de_fisiere_sortata)
