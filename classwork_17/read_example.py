# with open('example_multi_line.txt', 'w') as file:
#     for a in range(10):
#         file.write(f"a: {a}\n")

with open('example_multi_line.txt', 'r') as file:
    print(file)
    data = file.read()

print(data)

for line in data.splitlines():
    a, number = line.split(': ')
    if int(number) % 2 == 0:
        print(line)

with open('example_multi_line.txt', 'r') as file:
    print(file)
    data = file.read()
    print(data)
    file.seek(0)
    data_another_time = file.read()
    print('dat', data_another_time)
