def get_n_numbers_from_input(n) -> list[float]:
    list_of_numbers = []
    while len(list_of_numbers) < n:
        try:
            list_of_numbers.append(float(input('Enter a number')))
        except ValueError:
            print('Entered value was not a number')
    return list_of_numbers


result = get_n_numbers_from_input(10)
print(result)
