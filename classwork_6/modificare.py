nume_studenti = [
    "Marius",
    None,
    None,
    "Vitalie",
    "Alin",
    "Alex",
    "Vasile",
]
print(len(nume_studenti))

nume_studenti[1] = "Andrei"
print(nume_studenti)
nume_studenti[2] = "Mihai"
print("NS", nume_studenti)

also_nume_studenti = nume_studenti # .copy()
print("ANS", also_nume_studenti)

nume_studenti.append("Victor")
also_nume_studenti.remove("Marius")

print("NS", nume_studenti)

print("ANS", also_nume_studenti)
