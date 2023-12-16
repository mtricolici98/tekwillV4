o_lista_de_studenti = []

cati_studneit = int(input("Nr. Studenti"))

for nr_st in range(cati_studneit):
    nume = input(f'Nume student nr. {nr_st + 1}: ')
    nota = input(f'Nota student nr. {nr_st + 1}: ')
    o_lista_de_studenti.append(
        [nume, int(nota)]
    )

print(o_lista_de_studenti)
if o_lista_de_studenti:
    cea_mai_mare_nota = o_lista_de_studenti[0][1]

    for student_info in o_lista_de_studenti[1:]: # 4, 5, 8, 9, 5, 3, 9
        nota = student_info[1]
        if nota > cea_mai_mare_nota:
            cea_mai_mare_nota = nota

    # Toti studentii cu cea mai mare nota
    list_studenti = []
    for student_info in o_lista_de_studenti:
        if student_info[1] == cea_mai_mare_nota:
            list_studenti.append(student_info[0])

    print(
        f"Studentii cu cea mai mare nota ({cea_mai_mare_nota}) sunt {','.join(list_studenti)}"
    )
else:
    print('Nu sunt suficienti studenti')
