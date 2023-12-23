registru_elevi = {
    # "Ionel": []
}

while True:
    nume_elev = input("Numele elevului")
    try:
        nota_elev = int(input("Nota"))
    except:
        print("Nota invalida")
        continue

    if nume_elev not in registru_elevi:  # Cheia cu nume nu exista in dicitonar
        registru_elevi[nume_elev] = [nota_elev]
    else:
        registru_elevi[nume_elev].append(nota_elev)

    for elev_info in registru_elevi.items():
        nume, note = elev_info
        print(f"{nume} are media {sum(note) / len(note)}")
