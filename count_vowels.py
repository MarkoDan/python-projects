def main():
    while True:
        try:
            user_input = input('Enter a string: ')
            count_vowels(user_input)
        except ValueError:
            print('Invalid input, please enter a string')
        try:
            quit = input('Do you want to quit: y/n ')
            if quit.lower() == 'y':
                exit()
            elif quit.lower() == 'n':
                continue
        except ValueError:
            print('Invalid input')

def count_vowels(string):
    string = string.lower()
    count = 0
    VOWELS = ['a', 'e', 'i', 'o', 'u']

    for vowel in string:
        if vowel in VOWELS:
            count += 1
    print(count)

if __name__ == '__main__':
    main()