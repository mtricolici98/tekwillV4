introduceti_informatio = input()

if introduceti_informatio.startswith('error 401:'):
    print('We have authenticatn error, ask for password and try again')
elif introduceti_informatio.startswith('error 404:'):
    print('Resource not found, try looking for something else')
else:
    print("Unknown error, dunno what to do")
