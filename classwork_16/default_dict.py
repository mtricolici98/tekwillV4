from collections import defaultdict


def initializaeza_nr_de_vieti_a_jucatorului():
    return 5


jucatori_si_viewti = defaultdict(initializaeza_nr_de_vieti_a_jucatorului)

print(jucatori_si_viewti['Marius'])
jucatori_si_viewti['Marius'] -= 1
jucatori_si_viewti['Marius'] -= 1
print(jucatori_si_viewti)
jucatori_si_viewti['Andrei'] -= 1
print(jucatori_si_viewti)

cuvinte = dict()
text = 'Un text destul de lung'
for cuvant in text.split():
    if cuvant in cuvinte:
        cuvinte[cuvant] += 1
    else:
        cuvinte[cuvant] = 1

cuvinte = defaultdict(int)
text = 'Un text destul de lung, chiar foarte lung, de exemplu'
for cuvant in text.split():
    cuvinte[cuvant] += 1
print(cuvinte)

from collections import Counter

counter = Counter(text.split())
print(counter)


