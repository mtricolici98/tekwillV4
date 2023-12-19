list_of_numbers = input('CSV Numbers').split(',')
print(list_of_numbers)
new_list = []
for str_number in list_of_numbers:
    if str_number.isnumeric():
        new_list.append(int(str_number))
print(new_list)

print(list_of_numbers)
new_list = [int(str_nr) for str_nr in list_of_numbers if str_nr.isnumeric()]
print(new_list)

tabel = [
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 5],
    [1, 2, 3, 7],
]

names_of_students = [sum(el) for el in tabel]
print(names_of_students)

# sum = 0
# for a in new_list:
#     sum += a
# print(f'Suma este {sum}')
