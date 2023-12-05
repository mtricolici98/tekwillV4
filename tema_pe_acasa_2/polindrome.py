"""
Verificati daca un cuvant (sau serie de cuvinte) e un polindrom.

Un polindrom e un cuvand care se citeste la fel invers.
"""
# Pas 1
cuvant = input("Cuvantul pentru verificare").lower()
cuvant = cuvant.replace(" ", '')

# Pas 2
cuvant_invers = cuvant[::-1]  # Inversez cuvantul
print(cuvant_invers)
# Pas 3
print(cuvant == cuvant_invers)
