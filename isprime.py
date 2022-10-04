def check_number(number):
    number = int(number)
    if number <= 0 or number == 1:
        print('The number is not prime')
    i = 2
    while(i <= number ** 0.5):
        if number % i == 0:
            print('The number is not prime')
        else:
            print('The number is prime')
        i += 1
    


def main():
    while True:
        number = input('Please enter a number: ')
        if not number.isdecimal():
            print('Please enter a valid number')
        else:
            number = int(number)
            check_number(number)


main()