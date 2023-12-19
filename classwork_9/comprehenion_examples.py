lista_de_studenti = ['Marius', 'Ion', 'Gheorghe', 'Alexdra', 'Mariana']

studenti_prezenti = input().split()

studenti_absenti = [studen for studen in lista_de_studenti if studen not in studenti_prezenti]
print(f'Absenti au fost {studenti_absenti}')
