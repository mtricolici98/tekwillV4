"""
Shopping Cart Application:
Develop a basic shopping cart application that allows users to add items, view their cart, and calculate the total cost.
Use lists to store the items and their quantities, and dictionaries to maintain the item details and prices.
Implement functions to add items, display the cart, and calculate the total cost.

* The application should allow users to add items to their cart by providing item IDs, quantities, and prices.
* The application should maintain a list of items in the cart, including item details and quantities.
* The application should provide a function to display the contents of the cart, including item names, quantities,
 and total cost.
* The application should calculate the total cost of all items in the cart based on their quantities and prices.
"""

# 1. Cream o lista de produse initiale; Apoi le adaugam in cos
# 2. Cand adaugam in cos, verificam daca produsul este cunoscut si modificam cosul.
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

# pretul
# cos[element] * lista_de_produse[element]

while True:
    print('Choose the number corresponding to your option')
    print('1. Add to cart')
    print('2. View Cart')
    print('3. Calculate total cost')
    print('ANULARE: Remove an element')
    print('Type quit to quit the program')
    main_option = input('Choose: ')
    match main_option:
        case '1':
            while True:
                print('Alege elemtnul din cos pentru adaugare')
                for nume, pret in produse_si_pret.items():
                    print(f'{nume:^16}|{pret:^16}| Disponibil: {stock[nume]}')
                optiune = input('Alege produsul sau scrie stop: ')
                if optiune == 'stop':
                    break
                if optiune not in produse_si_pret:
                    print('Produs inexistent, incearca din nou')
                    continue
                cantitate = int(input(f'Ce cantitate de {optiune}: '))
                nivel_stock = stock[optiune]
                if cantitate >= nivel_stock:
                    print(f'In stock sunt doar {nivel_stock} {optiune}')
                    continue
                if cantitate <= 0:
                    print("Cantiate invalida")
                    continue
                if optiune in cos:
                    cos[optiune] += cantitate
                else:
                    cos[optiune] = cantitate
                stock[optiune] -= cantitate

        case '2':
            print('Produs | Cantitate | Suma')
            for nume, cantitate in cos.items():
                print(f'{nume:^16}|{"x" + str(cantitate):^16}|{cantitate * produse_si_pret[nume]}')

        case 'ANULARE':
            while True:
                if not cos:
                    print('Nu sunt elemente in cos')
                    break
                print('Alege elemtnul din cos pentru adaugare')
                for nume, pret in cos.items():
                    print(f'{nume:^16}|{pret:^16}| Disponibil: {stock[nume]}')
                optiune = input('Alege produsul sau scrie stop: ')
                if optiune == 'stop':
                    break
                if optiune not in cos:
                    print('Produs inexistent, incearca din nou')
                    continue
                cantitate = int(input(f'Ce cantitate de {optiune}: '))
                cantitatea_in_cos = cos[optiune]
                # Eliminam maximum cat este in cos
                cantitate_eliminare = min(cantitate, cantitatea_in_cos)
                stock[optiune] += cantitate_eliminare
                cos[optiune] -= cantitate_eliminare
                if cos[optiune] <= 0:
                    cos.pop(optiune)

        case '3':
            print('Produs | Cantitate | Suma')
            total = 0
            for nume, cantitate in cos.items():
                suma_produs = cantitate * produse_si_pret[nume]
                print(f'{nume:^16}|{"x" + str(cantitate):^16}|{suma_produs}')
                total += suma_produs
            print(f'Total pentru cos: {total}')
        case 'quit':
            break
