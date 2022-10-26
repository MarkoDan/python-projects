cost = 50
while True:
    print(f'Amount Due: {cost}')
    user_input = int(input('Insert Coin: '))
    if cost - user_input != 0:
        cost = cost - user_input
        print(f'Amount Due: {cost}')

    else:
        cost = 0
        print(f'Change Owed {cost}')
        break

