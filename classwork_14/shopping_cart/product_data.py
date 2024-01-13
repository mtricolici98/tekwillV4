stock = {
    "Banana": 100,  # In total 100 de banane in magazin
    "Ciocolata": 30,
    "Ingetata": 25,
    "Vin": 70,
}

produse_si_pret = {
    "Banana": 10,
    "Ciocolata": 30,
    "Ingetata": 25,
    "Vin": 70,
}

cos = {
    # "Banana": 5
}


def display_item_information_view(product_dict):
    for nume, pret in product_dict.items():
        print(f'{nume:^16}|{pret:^16}| Disponibil: {stock[nume]}')


