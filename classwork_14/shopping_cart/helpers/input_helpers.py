def get_input_or_stop_view():
    optiune = input('Alege produsul sau scrie stop: ')
    if optiune.lower() == 'stop':
        return True, None
    return False, optiune


def get_strict_number_view(message="Intordu un numar: "):
    while True:
        try:
            print()
            value = int(input(message))
            print()
            return value
        except ValueError:
            print('Se cere o valoare numerica')


if __name__ == '__main__':
    a = get_strict_number_view()
    print(a)
