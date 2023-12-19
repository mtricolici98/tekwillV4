import string

propozitie = input('Introducem o prozitie')

nr_consoane = 0
numar_vocale = 0
nr_total_caracter = 0

for charater in propozitie:
    if charater in string.punctuation + string.whitespace + string.digits:
        print('Caracterul nu este o litera')
        continue

    if charater.lower() in 'ayioue':
        numar_vocale += 1
    else:
        nr_consoane += 1
    nr_total_caracter += 1

print(nr_total_caracter, numar_vocale, nr_consoane)
