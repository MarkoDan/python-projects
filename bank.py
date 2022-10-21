def main():
    while True:
        check_greeting()
        ask_user = input('Do you want to continue? y/n ')
        ask_user = ask_user.lower()
        if ask_user == 'y':
            continue
        else:
            break


def greeting():
    while True:
        user_input = input('Greeting: ')
        if user_input.isdigit():
            print('Invalid Input')
            continue

        return user_input


def check_greeting():
    user_input = greeting()
    response = user_input.lower().strip()
    amount = 0
    if response.startswith('hello'):
        print('$0')
        amount += 0
    elif response.startswith('h'):
        print('$20')
        amount += 20
    else:
        print('$100')
        amount += 100




main()