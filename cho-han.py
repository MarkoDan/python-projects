import random
import sys

purse = 5000
while True:
    print(f'You have {purse} how much you want to bet? (q for QUIT)')
    pot = input('> ')
    if pot == 'q':
        sys.exit()
    elif not pot.isdecimal():
        print('Please enter a number')
    elif int(pot) > purse:
        print('You do not have enough to make that bet.')
    else:
        pot = int(pot)
        break
    
    #Roll the dice
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print('CHO (even) or HAN (odd)?')
bet = input("> ")
while True:
    if bet != "CHO" or bet != "HAN":
        print('Please enter a valid input')
        continue
    else:
        break
print(f'The first dice: {dice1}: ')
print(f'The second dice: {dice2}')

rolls_even = (dice1 + dice2) % 2 == 0
if rolls_even:
    correctBet = 'CHO'
else:
    correctBet = 'HAN'

playerWon = bet == correctBet

if playerWon:
    print('You won')