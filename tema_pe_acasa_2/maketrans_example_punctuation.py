"""
Cu ajutorul la maketrans, creezi un tabel ( cu 2 randuri )
pe primul rand sunt elementele care sa fie inlocuite (x),
pe al doilea (y) cu ce sa fie inlocuite.

metoda translate apoi aplica aceasta "traducere"
"""

txt = "H!?><.12,9812?!"

x = "?,.!;'|"  # 7 Semne de punctuatie
y = "       "  # 7 Locuri libere

print(x[0], 'va fi inlocuit cu', y[0])
print(x[1], 'va fi inlocuit cu', y[1])
print(x[2], 'va fi inlocuit cu', y[2])
# ... etc...

mytable = str.maketrans(x, y)

print(txt.translate(mytable))
