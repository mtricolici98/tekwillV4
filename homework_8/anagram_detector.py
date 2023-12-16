"""
Write a program that takes 2 separate words as input.

The program should check if the two words are anagrams.

Anagrams are words that can have their letters re-aranged to form another word.

Examples:

    dormitory → dirty room
    debit card → bad credit
    angered → enraged
    funeral → real fun
"""

word_1 = 'dormitory,.;'
word_2 = 'dirty             room'

import string

for el in string.whitespace + string.punctuation:
    word_1 = word_1.replace(el, '')
for el in string.whitespace + string.punctuation:
    word_2 = word_2.replace(el, '')

print(''.join(sorted(word_1.replace(' ', ''))))
print(''.join(sorted(word_2.replace(' ', ''))))
