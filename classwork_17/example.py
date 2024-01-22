import os.path

try:
    my_file = open('example.txt', 'w')
    my_file.write('Hello world')
    # Do some stuff
    raise Exception('Something happened')
    my_file.close()
except Exception:
    pass

# my_file = open('...')

with open('example.txt', 'r+') as my_file:
    print(my_file.read())
    my_file.write('Some more information')

print('Aici eu am inchis fisierul')

with open('example1.txt', 'w+') as my_file:
    my_file.write('Some info')
    print(my_file.read())

if not os.path.exists(os.path.join(os.getcwd(), 'some_info')):
    os.makedirs(os.path.join(os.getcwd(), 'some_info'))
open('some_info/file.txt', 'w')
