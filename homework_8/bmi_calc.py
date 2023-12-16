greut = float(input('introdu greutatea (kg): '))
inalt = float(input('introdu inaltimea (m): '))
bmc = greut / (inalt * inalt)

if bmc < 18.5:
    print('Subponderalitate')
elif bmc <= 24.9:
    print('Greutate normala')
elif bmc <= 29.9:
    print('Excesul de greutate')
else:
    print('Obezitate')
print(f'IMC = ', bmc)
