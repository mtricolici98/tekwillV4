vowels = 'aouyie'
cuvinte = ['capra', 'marius', 'rinocer']
for cuvant in cuvinte:
    print(F'Procesez {cuvant}')
    suma_de_vocale = 0
    for litera in cuvant:
        if litera in vowels:
            suma_de_vocale += 1
    print(f"Cuvantul {cuvant} are {suma_de_vocale} vocale")
