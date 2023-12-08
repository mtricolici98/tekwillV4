string_mare = input("Textul: ")
caracter = input("Carcaterul: ")
print(f"Caracterul {caracter} se intalneste in text de "
      f"{string_mare.lower().count(caracter.lower())} ori.")
