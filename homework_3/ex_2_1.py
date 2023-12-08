initial_string = input("Type in your string: ")

print(initial_string)

x = '!@#$%^&*()-=_+\';":?.,{}[]1234567890/'
y = ' ' * len(x)
translation_table = str.maketrans(x, y)

clean_string = initial_string.lower().translate(translation_table).replace(' ', '')

print(clean_string)

# Vocale: aieouy
vowel_count = clean_string.count('a')
vowel_count += clean_string.count('i')
vowel_count += clean_string.count('e')
vowel_count += clean_string.count('o')
vowel_count += clean_string.count('u')
vowel_count += clean_string.count('y')

print(f"Nr total de litere:", len(clean_string))
print(f"Nr total de vocale:", vowel_count)
print(f"Nr total de consoane:", len(clean_string) - vowel_count)
