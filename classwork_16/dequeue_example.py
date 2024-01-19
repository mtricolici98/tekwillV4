from collections import deque

my_queue = deque(['Ion', "Marin"])

while my_queue:
    utilizator = my_queue.popleft()
    print(f"Il procesez pe {utilizator}")
    om_nou_in_rand = input('New user ?')
    if om_nou_in_rand:
        is_premium = input('Il premium ?') == 'y'
        if is_premium:
            my_queue.appendleft(om_nou_in_rand)
        else:
            my_queue.append(om_nou_in_rand)
    print('In rand au ramas', my_queue)

from decimal_example import Decimal

print(Decimal("1.5123125123"))
print(Decimal(1.1))
print(Decimal("1.1"))
print(Decimal("1.1") * 2)
