import os


def max(*numbers, limit=100):
    if len(numbers) == 0:
        return None
    my_max = numbers[0]
    for nr in numbers:
        if nr > my_max:
            my_max = nr
    return my_max if my_max < limit else limit


print(max(50, 60, 120, 240, limit=120))


#
# def delete_files(*files):
#     for f in files:
#         os.remove(f)
#
#
# delete_files('test.txt', 'test.txt', 'test.txt', 'test.txt')

more = (1, 5, 6)

a, b, c = more
print(a, b, c)

print(more)
print(*more)

list_of_tuples = [
    (1, 2),
    (2, 3)
]
print(list_of_tuples)

for tup in list_of_tuples:
    print(tup)

for a, b in list_of_tuples:
    print(a)
    print(b)

dictionary = {
    1: 'one',
    2: 'two',
    3: 'three',
}

print(dictionary.items())
for key, value in dictionary.items():
    print(key, value)

for info in dictionary.items():
    print(info)

print(1, 2, 3, 4, sep=' | ')


