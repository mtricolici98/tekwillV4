my_set = set()
my_set = set([1, 2, 3, "123"])
print(my_set)


class NumberSet(set):

    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self._validate_data(initial_data)
        super().__init__(initial_data)

    def add(self, element):
        self._validate_data([element])
        super().add(element)

    def update(self, iterable):
        self._validate_data(iterable)
        super().update(iterable)

    def symmetric_difference_update(self, iterable):
        self._validate_data(iterable)
        super().symmetric_difference_update(iterable)

    def _validate_data(self, iterable):
        for element in iterable:
            if not isinstance(element, (int, float)):
                raise TypeError("Number set only allows numeric values")


my_nr_set = NumberSet([1, 2, 3, 3, 3])
print(my_nr_set)
my_nr_set.add(5)
print(my_nr_set)
my_nr_set.update([123])
print(my_nr_set)
try:
    my_nr_set.symmetric_difference_update(["123"])
    print("Hello")
except TypeError:
    print("Bye")
print(my_nr_set)
