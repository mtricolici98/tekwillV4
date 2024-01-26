def example(arg, *args: tuple[int]):
    print(arg)
    print(args)
    # for el in args:
    #     if type(el) != int:
    #         raise TypeError("Argument must be an integer")


print(example(10, '1', '2', '3'))

values = list(range(1000))
print(values)
a, b, c, *remainder = values
print(a, b, c)
print(remainder)
print(values)
