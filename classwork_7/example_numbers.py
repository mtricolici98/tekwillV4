user_input = input()  # 10.4, 10, zece
# INcerc sa vad daca e int, daca nu incerc sa vad daca e float
potential_numer = None
try:
    potential_numer = int(user_input)
except ValueError:  # Nu e int
    try:
        potential_numer = float(user_input)
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        if 'zece' in str(ex):
            potential_numer = 10
        else:
            print('Value is not a valid number')
            raise ex

print(potential_numer)
