sentence = input("Propozitia ?").lower()
if len(sentence) < 2:
    print("propoztia e prea scurta")
    exit()

char = input("Caracterul").lower()
if len(char) != 1:
    print("E nevoie de un singur caracter")
    exit()

# avem o propozitie si avem un singur caracter
# Exemplu: Asa se face (a)
result = sentence.find(char)  # -1 sau indexul - 0
if result >= 0:
    character_occurences = [str(result + 1)]
else:
    character_occurences = []

while result >= 0:  # -1 >= 0
    start = result + 1  # Start devine 1 ; 3; 10
    result = sentence.find(char, start)  # - 2; 9; -1
    if result >= start:  # - 2 >= 1; 9 >= 3; -1 >= 10 - Fals
        character_occurences.append(str(result + 1))

if character_occurences:
    textul_occurences = ", ".join(character_occurences)
    print(f"Acest caracter a fost intalnit de {len(character_occurences)} ori pe pozitiile: {textul_occurences}")
else:
    print("Acest caracter nu a fost intalnit de-loc")
