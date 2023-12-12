datornici = ["Marius", "Ion", "Vassile", "Alin", "Vitalie"]
sume_datornici = [10, 15, 13, 4, 12]

for name in datornici:
    print(name)

# indice = [0, 1, 2]
# for index in indice:
#     print(f'Datornicul nr {index + 1} este {datornici[index]} si datoreaza {sume_datornici[index]}')

for index in range(len(datornici)):
    print(f'Datornicul nr {index + 1} este {datornici[index]} si datoreaza {sume_datornici[index]}')

for time in range(3):
    datornici.append(input("name"))
    sume_datornici.append(input("suma"))


for index in range(len(datornici)):
    print(f'Datornicul nr {index + 1} este {datornici[index]} si datoreaza {sume_datornici[index]}')
