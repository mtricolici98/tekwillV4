my_data = 'ASdjhajkshejahs!,.'

lower_data = my_data.lower()
no_exclamation = lower_data.replace("!", '')
no_space = no_exclamation.replace(" ", '')
count_as = no_space.count('a')

print(
    my_data.lower().replace('!', '').replace(' ', '')
    .count('a')
)

input_number = int(input(input("What to ask user")))
input_number = int("10")
