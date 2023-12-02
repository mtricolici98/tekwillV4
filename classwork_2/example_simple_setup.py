variable = '123123'

print(len(variable))

print()
print("!", "?", "?", "!")

len("1")

# a = input()
# if type(a) == str:
#     print("a is a string")

print("It's me \"Mario\"")

print('She said \n"What ?!"' * 3)
print("Really ?")

a = """
Asta e texxt, care e formata ca in notepad
De exemplu: 
nu conteaza cat scrii ''' '/ " "
"""

a = 1
b = 2
print("Rezultatul adunarii intre " + str(a) + " si " + str(b) + " va fi " + str(a + b))

print(f"Resultatul adunarii intra {a} si {b} este {a + b}")

print("Resultatul adunarii intra {} si {} este {}".format(a, b, a + b))

username = input("Username? ")
email = ""

multiline_f_string = f"""
Stimate {username[:25]}, 

Bine ai venit.
"""
print(multiline_f_string)


