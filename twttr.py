vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    user_input = str(input('Input: '))
    for i in user_input:
        if i.lower() in vowels:
           user_input = user_input.replace(i, '')
    print(f'Output: {user_input}')