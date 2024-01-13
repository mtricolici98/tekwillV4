from helpers.input_helpers import get_input_or_stop_view, get_strict_number_view
from product_data import display_item_information_view


def adauga_produs_in_cos(product, cantitate, dictionar_stock, dictionar_cos):
    nivel_stock = dictionar_stock[product]
    if cantitate > nivel_stock:
        print(f'In stock sunt doar {nivel_stock} {product}')
        return
    if cantitate <= 0:
        print("Cantiate invalida")
        return
    if product in dictionar_cos:
        dictionar_cos[product] += cantitate
    else:
        dictionar_cos[product] = cantitate
    dictionar_stock[product] -= cantitate


def elimina_produs_din_cos(product, cantitate, dictionar_stock, dictionar_cos):
    cantitatea_in_cos = dictionar_cos[product]
    # Eliminam maximum cat este in cos
    cantitate_eliminare = min(cantitate, cantitatea_in_cos)
    dictionar_stock[product] += cantitate_eliminare
    dictionar_cos[product] -= cantitate_eliminare
    if dictionar_cos[product] <= 0:
        dictionar_cos.pop(product)


def add_product_to_cart_view(dictionar_produse, dictionar_stock, dictionar_cos):
    while True:
        print('Alege elemtnul din cos pentru adaugare')
        display_item_information_view(dictionar_produse)
        stop, optiune = get_input_or_stop_view()
        if stop:
            break
        if optiune not in dictionar_produse:
            print('Produs inexistent, incearca din nou')
            continue
        cantitate = get_strict_number_view(f"Introdu cantitate de {optiune}")
        adauga_produs_in_cos(optiune, cantitate, dictionar_stock, dictionar_cos)


def remove_from_cart_view(dictionar_stock, dictionar_cos, dictionar_produse):
    while True:
        if not dictionar_cos:
            print('Nu sunt elemente in cos')
            break
        print('Alege elemtnul din cos pentru adaugare')
        display_cart_items(dictionar_cos, dictionar_produse)
        stop, optiune = get_input_or_stop_view()
        if stop:
            break
        if optiune not in dictionar_cos:
            print('Produs inexistent, incearca din nou')
            continue
        cantitate = get_strict_number_view()
        elimina_produs_din_cos(optiune, cantitate, dictionar_stock, dictionar_cos)


def display_cart_items(cart_dict, product_dict):
    print()
    print(f'{"Produs":^16}|{"Cantitatea":^16}|{"Suma":^16}')
    for nume, cantitate in cart_dict.items():
        print(f'{nume:^16}|{"x" + str(cantitate):^16}|{cantitate * product_dict[nume]:^16}')
    print()


def show_total_view(product_dict, cart_dict):
    print('\nTOTAL:')
    total = 0
    for nume_produs, cantitate in cart_dict.items():
        pretul = product_dict[nume_produs]
        total += cantitate * pretul

    display_cart_items(cart_dict, product_dict)
    print(f'Total pentru cos: {total}')
    print()
