import string
import random

all_letters = list(string.ascii_letters + string.digits + string.punctuation)
pass_length = int(input('Pass length'))

password = ''
for a in range(pass_length):
    letter_index = random.randrange(0, len(all_letters))
    password += all_letters[letter_index]

print(password)
