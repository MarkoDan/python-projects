def main():
    while True:
        try:
            number = int(input('Enter a number: '))
            conjecture(number)
        except ValueError:
            print('Invalid input')

def conjecture(n):
    if n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    print(n)


if __name__ == '__main__':
    main()
