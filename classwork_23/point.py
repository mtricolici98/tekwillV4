class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        if self.x < other.x:
            return True
        if self.x > other.x:
            return False
        if self.y < other.y:
            return True
        return False

    def __bool__(self):
        return not (self.x == 0 and self.y == 0)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Point(self.x * other, self.y * other)
        raise TypeError(f"Cannot multiply {type(other)} with point")


p = Point(1, 2)
p.x += 3
print(p)

p2 = Point(2, 3)
print(p > p2)

list_of_points = [Point(1, 2), Point(3, 4), Point(-2, 4)]
print(list_of_points)

list_of_points.sort()
print(list_of_points)

zero = Point(0, 0)

non_zero = zero + p + p
print(non_zero)

if zero:
    print('zero is present')

if p:
    print('P is present')

other = Point(0, 1)
if other:
    print('other is present')

print(other * p * p)
print(p * 10)
print(p * 1.1)


df_1 = ...
df_2 = ...

df1 + df2

