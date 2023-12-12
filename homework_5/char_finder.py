sentence = input("Propozitia ?")
if len(sentence) < 2:
    print("propoztia e prea scurta")
    exit()

char = input("Caracterul")
if len(char) != 1:
    print("E nevoie de un singur caracter")
    exit()

# varianta cu find
char_in_sentence = sentence.find(char)
if char_in_sentence >= 0:
    print(f"Caracterul {char} se gaseste pe poztia {char_in_sentence + 1} in text.")
else:
    print(f"Caracterul nu este in text")

# varianta cu find
if char not in sentence:
    print(f"Caracterul nu este in text")
else:
    char_in_sentence = sentence.index(char)
    print(f"Caracterul {char} se gaseste pe poztia {char_in_sentence + 1} in text.")
