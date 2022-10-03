
def bank_loan():
    while True:
        loan = input('Please enter the amount of your loan: ')
        if loan.isdecimal():
            break
        else:
            print('Please enter valid number.')
    return int(loan)

def fixed_rate():
    while True:
        rate = input('Please enter the number of years, that you will pay out your loan: ')
        if rate.isdecimal():
            break
        else:
            print('Please enter a valid number.')
    return int(rate)


def main():
    while True:
        print('Welcome to Mortgage Calculator')
        loan = bank_loan()
        rate = fixed_rate()
        anual_mortgage = loan / rate
        monthly_mortgage = anual_mortgage / 12
        user_choise = input('Please enter M for Monthly Mortgage or enter A for anual.')
        if user_choise == "M":
            print(f'Your monthly mortgage will be {monthly_mortgage}$')
        elif user_choise == "A":
            print(f"Your anual mortgage will be {anual_mortgage}$")

    
main()