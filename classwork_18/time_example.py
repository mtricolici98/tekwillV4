import time


def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


start = time.time()
is_prime(79191312345)
time.sleep(0.5)
end = time.time()
print("A durat", end - start)

i = 0
while True:
    print(i)
    i += 1
    time.sleep(1)
