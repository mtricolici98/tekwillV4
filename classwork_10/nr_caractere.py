string = input("?")

char_info = {}

for char in string:
    if char in char_info:
        char_info[char] += 1
    else:
        char_info[char] = 1

print(char_info)
