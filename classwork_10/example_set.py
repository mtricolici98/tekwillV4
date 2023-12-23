cos_meu = {'Paine', "CHips", "bere", 'bere', 'peste'}
cosul_lui_ion = {'Paine', 'peste', 'bomboane'}

print(cos_meu.union(cosul_lui_ion))

print(cos_meu.intersection(cosul_lui_ion))

print(cos_meu.difference(cosul_lui_ion))
print(cosul_lui_ion.difference(cos_meu))

print(cos_meu - cosul_lui_ion)
print(cosul_lui_ion - cos_meu)

print(cos_meu.symmetric_difference(cosul_lui_ion))
