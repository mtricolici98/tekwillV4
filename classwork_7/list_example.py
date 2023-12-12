# code_in_exercise = open('example_numbers.py').readlines()
# for line_of_code in code_in_exercise:
#     print(line_of_code)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number % 2 == 0:
        print(number)

for number in range(1, 10):
    if number % 2 == 0:
        print(number)


for time in range(5):
    print(f'I am doing this {time + 1} time out of 5 times')
