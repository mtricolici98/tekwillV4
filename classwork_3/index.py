my_string = "ABCDKJASKJDASD"
print(len(my_string))
print("last index is", len(my_string) - 1)
last_char = my_string[len(my_string) - 1]
last_char = my_string[-1]
# last_char = my_string[len(my_string)] # Eroare
last_char = my_string[-15:4]
print(last_char)

print(my_string[1])
print(my_string[2])
print(my_string[4])

# my_string[1] = "U"
my_string = "ABCDKJASKJDASD"
char_to_replace = 2
string_nou = my_string[0:char_to_replace] # ABC
string_nou += "P" # ABCU
string_nou += my_string[char_to_replace + 1:]
print(string_nou)

my_string = "Alta valoare"
