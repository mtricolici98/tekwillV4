products_in_stock = [
    'paine', 'orez', 'rosii', 'portocale', 'mandarine'
]  # Livrare in 1 zi

products_in_warehouse = [
    'trufe', 'casvaval', 'mandarine'
]  # Livrare in 2 zile

produsct_only_in_warehouse = [p for p in products_in_warehouse if p not in products_in_stock]
print("POIW", produsct_only_in_warehouse)
produse_disponibile = products_in_warehouse + products_in_stock

cos_de_cumparaturi = []
timp_livrare = 0
condition = True
while condition:
    produsul = input()
    if produsul == 'stop':
        break
    if produsul not in produse_disponibile:
        print("Produsul nu este disponibil pentru comanda")
        continue
    cos_de_cumparaturi.append(produsul)
    if produsul in products_in_stock and timp_livrare <= 1:
        timp_livrare = 1
    else:
        timp_livrare = 2

print(f"Cosul este {cos_de_cumparaturi} si va fi livrat in {timp_livrare} zile.")
