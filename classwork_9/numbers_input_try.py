run = True
numbers_list = []
while run:
    potential_number = input('Introdu un numar sau STOP')
    if potential_number.lower() == 'stop':
        break
    try:
        valid = float(potential_number)
    except ValueError:
        print(f"Value is not a number")
        continue
    numbers_list.append(potential_number)

print(f"Lista este")
print(numbers_list)
