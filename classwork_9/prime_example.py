nr_of_prime_nrs = int(input("N"))
for number_to_check in range(nr_of_prime_nrs):
    is_prime = True
    for div in range(2, number_to_check // 2 + 1):
        if number_to_check % div == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{number_to_check} Is prime')
    else:
        print(f'{number_to_check} Is not prime')
