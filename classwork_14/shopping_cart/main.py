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
from cart import add_product_to_cart_view, display_cart_items, remove_from_cart_view, show_total_view
from product_data import *


def main():
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
                add_product_to_cart_view(produse_si_pret, stock, cos)
            case '2':
                display_cart_items(cos, produse_si_pret)
            case 'ANULARE':
                remove_from_cart_view(stock, cos, produse_si_pret)
            case '3':
                show_total_view(produse_si_pret, cos)
            case 'quit':
                break


main()
