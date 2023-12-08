age = int(input())
parents_present = input("Are parents present ? Y/N").upper() == 'Y'

REQ_AGE = 14
if age >= REQ_AGE or parents_present:
    print('You are allowed to see the movie')
else:
    print('You should be at least 14 or be with your parents to see the movie')

age = int(input())
parents_present = input("Are parents present ? Y/N").upper() == 'Y'

REQ_AGE = 14
if age >= REQ_AGE and parents_present:
    print('You are allowed to see the movie')
else:
    print('You should be at least 14 or be with your parents to see the movie')
