elevi = [
    ("Marius", 'Tricolic'),
    ("Igor", "Dodon"),
    ("Vlad", "Filat")
]

registru_de_note = dict()
for elev in elevi:
    print(f"Introduceti notele pentru {elev}")
    lista_note = []
    while True:
        nota = input('Nota')
        try:
            nota = int(nota)
        except:
            break
        lista_note.append(nota)
    registru_de_note[elev] = lista_note

for elev in registru_de_note:
    print(f"Elevul {elev} are nota {registru_de_note[elev]}")
