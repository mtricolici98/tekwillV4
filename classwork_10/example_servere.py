server_vechi = {1, 2, 3}
server_noi = {3, 4, 2}

print(f"Trebuie sa adaug {server_noi.difference(server_vechi)}")

print(f"Trebuie sa elmin {server_vechi.difference(server_noi)}")

print(f"Trebuie sa nu ating {server_vechi.intersection(server_noi)}")

for el in server_noi:
    print(el)
