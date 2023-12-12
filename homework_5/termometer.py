temperatura = int(input("Introduceti temperatura: "))

if temperatura <= -10:
    print("Extrem de frig")
elif temperatura <= 0:
    print("Frig")
elif temperatura <= 10:
    print("Rece")
elif temperatura <= 20:
    print("Confortabil")
elif temperatura <= 30:
    print("Cald")
elif temperatura <= 40:
    print("Extrem de cald")
else:
    print("Apocalipsă")


temperature = int(input('Please input the temperature: '))
if temperature <= -10:
    print('Extremely freezing')
if temperature > -10 and temperature <= 0:
    print('Freezing')
if temperature > 0 and temperature <= 10:
    print('Cold')
if temperature > 10 and temperature <= 20:
    print('Comfortable')
if temperature > 20 and temperature <= 30:
    print('Warm')
if temperature > 30 and temperature <= 40:
    print('Extremely Warm')
if temperature > 40:
    print('Apocalypse')
