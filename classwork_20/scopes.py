import random

global_varibale = 10  # Imutable


def print_global_varibale():
    global global_varibale  # Imutabile
    global_varibale = 15
    print(global_varibale)


print_global_varibale()
print(global_varibale)

mutable_global = set()  # Mutable


def add_to_set_and_print():
    mutable_global = set()
    mutable_global.add(random.randint(1, 1000))
    print(mutable_global)


print(add_to_set_and_print())
print(mutable_global)
print(add_to_set_and_print())
print(mutable_global)
