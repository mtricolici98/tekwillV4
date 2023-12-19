# Create a program that will show all combination of a, b, c where a + b + c = N
# N este introdus de la consola si este numar natural mai mare ca 3
# A, B, C nu egale intre ele si > 0
N = int(input('Number: '))
counter = 0
results = []
# N = 6
# a = 3
# b >= 3

for a in range(1, N):
    for b in range(1, N - a):
        counter += 1
        if b == a:
            continue
        c = N - a - b
        if c == b or c == a:
            continue
        if a + b + c == N:
            print(a, b, c)
            results.append((a, b, c))

print(counter)
print(len(results))
