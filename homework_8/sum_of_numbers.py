sum_even = sum_odd = total = 0
numbers_input = input("Please type a list of numbers separated by comma : ")
list_of_numbers = numbers_input.split(',')
for i in list_of_numbers:
    i = int(i)
    if not i % 2:
        sum_even += i
    else:
        sum_odd += i
    total += i

print(list_of_numbers)
print("The sum of all even numbers = ", sum_even)
print("The sum of all odd numbers = ", sum_odd)
print("The sum of all even numbers = ", total)
