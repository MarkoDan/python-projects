
def principle():
    while True:
        loan = input('Please enter the amount of your loan: ')
        if loan.isdecimal():
            break
        else:
            print('Please enter valid number.')
    return int(loan)

def how_many_years():
    while True:
        rate = input('Please enter the number of years, that you will pay out your loan: ')
        if rate.isdecimal():
            break
        else:
            print('Please enter a valid number.')
    return int(rate)

def interest_rate():
    while True:
        interest_rate = input('Please enter the interest rate: ')
        if interest_rate.isdecimal():
            break
        else:
            print('Please enter valid interest_rate')
    return int(interest_rate)

def calculate_mortgage():
    p =  principle()
    years = how_many_years()
    r = interest_rate()
    r = (r / 100) / 12
    n = 12 * years
    m1 = p * r * (1 + r) ** n
    m2 = (1 + r) ** n -1
    m = m1 / m2
    return m
def main():
    while True:
        print('Welcome to Mortgage Calculator')
        mortgage = calculate_mortgage()
        print(f"Your monthly mortgage is {mortgage}$")

    
main()