timp = input('Time in the format of HH:MM AM/PM')
if timp[-2:] not in ['PM', 'AM']:
    print('Eroare: format timp gresit')
    exit()

ora_corecta = timp[:-2].split(':')
if len(ora_corecta) != 2:
    print('Eroare: format timp gresit')
    exit()

try:
    ore, minute = int(ora_corecta[0]), int(ora_corecta[1])
except ValueError:
    print('Eroare: format timp gresit')
    exit()

if timp[-2:] == 'PM':
    if ore < 12:
        ore += 12
else:
    if ore == 12:
        ore -= 12

print(f"{ore:0>2}:{minute:0>2}")
