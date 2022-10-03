

def deposit():
    while True:
        deposit = input("How much would you like to deposit? $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("The deposit must be greated than 0")
        else:
            print("Please enter a number")


def get_bet():
    while True:
        amount = input("How much would you like to bet?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a valid amount")
        else:
            print("Please enter a number")


def main():
    balance = deposit()
    bet = get_bet()


