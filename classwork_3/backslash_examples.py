a_long_text = """asdasdhkajshd
asdasda
a
s
    da
sd
a
s"""

same_line_text = a_long_text.replace('\n', ' ')
print(same_line_text)

example = "Hello Darkness My Old Friend#!@#!@$!*@#*!&@$^*!@&#&*^!$"
example = example.replace(' ', '\n')
print(example)

print('Hello \\new friend')
print('Hello \'\'new friend')
print('Hello \nnew friend')
print()
print()
print()
print('Hello new friend'.replace('e', ''))
print('Hello new friend'.replace('o', ''))
print('Hello new friend'.replace('o', ''))

# avand caracterele a, b, c
# fa replace la fiecare din ele cu spatiu gol
# for char in 'abc':
#     string.replace(char, '')
