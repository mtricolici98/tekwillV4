def my_input():
    a = input('Some value:')
    return a


my_input()


def get_numbers_list_from_input():
    input_value = input("Enter a list of numbers")
    if not input_value:
        print('No input')
        return []  # Function has finished but no result
    list_of_str_nrs = input_value.split()
    list_of_numbers = []
    for element in list_of_str_nrs:
        try:
            list_of_numbers.append(float(element))
        except ValueError:
            print(f'Found element {element} which is not a number')
    return list_of_numbers


result = get_numbers_list_from_input()
print(sum(result))
for element in result:
    print(f'{element} is {type(element)}')
