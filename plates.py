def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')

def is_valid(plate):
    if len(plate) > 2 and len(plate) < 6:


main()
