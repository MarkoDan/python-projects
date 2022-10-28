def main():
    while True:
        try:
            array = list(input('Enter an array of numbers: '))
            merge_sort(array)
        except ValueError:
            print('Invalid input')

def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]

        #recursion
        merge_sort(left_array)
        merge_sort(right_array)

        #merge
        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                k += 1
            else:
                array[k] = right_array[j]

if __name__ == '__main__':
    main()