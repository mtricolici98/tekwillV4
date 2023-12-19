numbers_list = []
while True:
    potential_number = input('Introdu un numar sau STOP')
    if potential_number.lower() == 'stop':
        break

    if potential_number.isnumeric():
        numbers_list.append(potential_number)
        continue

    if '.' in potential_number:
        parts = potential_number.split('.')
        p_s, p_d = parts[0], parts[1]
        if len(parts) == 2 and p_s.isnumeric() and p_d.isnumeric():
            numbers_list.append(potential_number)
            continue

    print(f"Valoare nu este numerica")

print(f"Lista este")
print(numbers_list)
