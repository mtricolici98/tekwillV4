my_list = []
for a in range(0, 100):
    my_list.append(a)

my_data = tuple(my_list)
print(my_data)

my_even_numbers = tuple(el for el in my_data if el % 2 == 0)
print(my_even_numbers)

options = ['Today', 'Tomorrow', 'Never']

for option in options:
    pass

options_tuple = tuple(options)
options_list = list(options_tuple)
options_tuple = tuple(options_list)

my_Str = 'Hello Marius'
my_str_tuple = tuple(my_Str)
print(my_str_tuple)

import sys

player_stats = ("Marius", 15, ["Sabie"])
print(sys.getsizeof(player_stats))
print(sys.getsizeof(player_stats[2]))
print(player_stats)
nume, puncte, inventar = player_stats

puncte += 10

player_stats = (nume, puncte, inventar)
print(sys.getsizeof(player_stats))
print(player_stats)

player_stats[2].append("Mar")
print(sys.getsizeof(player_stats))
print(sys.getsizeof(player_stats[2]))
print(player_stats)

players_stats = (player_stats, player_stats, player_stats)

for tuple_El in players_stats:
    for element in tuple_El[2]:
        print(f"Elemnt din lista {element}")

for element in 100:
    print(element)
