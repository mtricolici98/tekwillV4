def print_list(my_list, symbol):
    for element in my_list:
        print(symbol, element, symbol)


def print_list_simple(my_list):
    for element in my_list:
        print('|', element, '|')


print_list([1, 2, 3, 4], "&")

print_list_simple([1, 2, 3, 4])

adaus_la_suma = 10


def sum_numbers(nr1, nr2):
    print(nr1 + nr2 + adaus_la_suma)

def dif_numbers(nr1, nr2):
    print(nr1 - nr2)

sum_numbers(1, 2)
dif_numbers(1, 2)
# dif_numbers('1', 2)
