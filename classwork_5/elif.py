daytime = False
lights_are_on = input("Lights on y/n") == 'y'
if daytime:
    print('Do nothing')
else:
    if not lights_are_on:
        print('>>Turn on lights!')

## Instead we can do

if not daytime and not lights_are_on:
    print('??Turn on lights')


if daytime == True:
    print('E ziua')

