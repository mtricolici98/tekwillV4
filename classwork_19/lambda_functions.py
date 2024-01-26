import os

persoane = [
    {'nume': "Marius", "age": 25},
    {'nume': "1", "age": 30},
    {'nume': "2", "age": 21},
    {'nume': "3", "age": 53},
]

print(persoane)


def get_age(element):
    return element['age']


def get_name(element):
    return element['nume']


persoane.sort(key=get_age)
print(persoane)
persoane.sort(key=get_name)
print(persoane)
print('------------')
persoane.sort(key=lambda element: element['age'])
print(persoane)
persoane.sort(key=lambda element: element['nume'])
print(persoane)

