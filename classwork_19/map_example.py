str_numbers = ['1', '2', '3']
int_numbers = [int(a) for a in str_numbers]
print(int_numbers)

int_numbers = list(map(int, str_numbers))
print(int_numbers)

int_numbers = list(map(lambda a: int(a) * 10, str_numbers))
print(int_numbers)


def map_function(a):
    print('Processing', a)
    return int(a)


#
#
for element in map(map_function, str_numbers):
    print(f'Working with {element}', type(element))

int_numbers = list(map(map_function, str_numbers))
for element in int_numbers:
    if element % 2 == 0:
        break
    print(f'Working with {element}', type(element))

# Example1
new_list = []
for element in str_numbers:
    new_list.append(map_function(element))

# Example2
int_numbers = list(map(map_function, str_numbers))



