in_rand = []
tip_pasaport = []
# Aflam cate persoane
numar_persoane = int(input('Cate persoane vor fi: '))

# Aflam cine sunt persoanele
for a in range(numar_persoane):
    in_rand.append(input(f'Persoana numarul {a + 1}'))
    # Inregristram pentru ficare persoana, tipul de Pasport
    tipul_pass = input(f'Tip pasport {in_rand[a]}: MD/EU')
    tip_pasaport.append(tipul_pass.upper())

print(in_rand)
print(tip_pasaport)

# Procesam fiecare persoana
for numar_persoana in range(len(in_rand)):
    persoana = in_rand[numar_persoana]
    tip_pasaport_persoana = tip_pasaport[numar_persoana]
    print(f'Verific pasaportul lui {persoana}')
    if tip_pasaport_persoana != 'MD':
        print(f'{persoana} a trecut verificare')
    else:
        print(f"{persoana} nu trece verificarea")
