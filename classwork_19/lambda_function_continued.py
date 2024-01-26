print('------------')
power_2 = lambda a: a ** 2

print(power_2(4))

print(power_2(6))
valoare_rezultat = power_2(4)
print(valoare_rezultat)

print('------------')
max_lambda = lambda a, b: a if a > b else b
print(max_lambda(5, 3))

from collections import defaultdict

d = defaultdict(lambda: 'Hello World')
print(d['1'])
