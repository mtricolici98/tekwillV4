def display_d(num):
    print("---------")
    if num == 1:
        print("|       |")
        print("|   X   |")
        print("|       |")
    elif num == 2:
        print("| X     |")
        print("|       |")
        print("|     X |")
    elif num == 3:
        print("| X     |")
        print("|   X   |")
        print("|     X |")
    elif num == 4:
        print("| X   X |")
        print("|       |")
        print("| X   X |")
    elif num == 5:
        print("| X   X |")
        print("|   X   |")
        print("| X   X |")
    elif num == 6:
        print("| X   X |")
        print("| X   X |")
        print("| X   X |")
    print("---------")


import random


def roll_dice(num_dice, num_faces):
    rolls = []
    total = 0
    for a in range(num_dice):
        roll = random.randint(1, num_faces)
        rolls.append(roll)
        total += roll
    return rolls, total


def display_dice(rolls):
    for i, roll in enumerate(rolls, start=1):
        # print(f"Zar {i}: {roll}")
        display_d(roll)


while True:
    try:
        num_dice = int(input("Câte zaruri există (numar): "))
        num_faces = int(input("Câte fețe are zarul (MAX = 6): "))
        break
    except ValueError:
        print("Introdu numar intreg")

while True:
    rolls, total = roll_dice(num_dice, num_faces)

    print("\nZaruri aruncate:")
    display_dice(rolls)
    print(f"\nSuma totală: {total}")

    stop = input("\nScrie STOP pentru a opri sau apasa Enter pentru a continua: ").lower()
    if stop == "stop":
        break
