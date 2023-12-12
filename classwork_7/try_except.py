finished = False
while not finished:
    number = None
    try:
        number = int(input('Introdu un numar: '))
        print(f"Am primit numarul {number}")
    except Exception:
        print("Introdu o valoare numerica")
    if number is not None:
        print(F"Numarul {number} la patrat este {number ** 2}")
        finished = True


