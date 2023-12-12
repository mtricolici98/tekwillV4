try:
    a = int(input('a:'))
    b = int(input('b:'))
    print(a / b)
except ZeroDivisionError:
    print('A avut loc impartirea cu 0 care e gresita')
except ValueError:
    print('Valoarea introdusa nu este numerica')
except Exception:
    print('Sa intimplat o eroare necunoscuta')
finally:
    print('Asta se intimpla indiferent de eroare')
