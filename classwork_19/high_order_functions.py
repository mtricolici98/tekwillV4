def my_map(elementele, functia_de_ruat):
    print('Voi executa functia:', functia_de_ruat.__name__)
    print('Voi executa functia:', functia_de_ruat.__doc__)
    for elem in elementele:
        functia_de_ruat(elem)


my_map([1, 2, 3], print)

my_map([1, 2, 3], lambda x: print(x * 2))
