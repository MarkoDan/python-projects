import time


nemo = ['nemo']
array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(1000000)]
def findNemo(array):
    t0 = time.time()
    for i in range(1,10000000000):
        if i == 1000000000:
            print('Found nemo')
            break
    t1 = time.time()
    print(f'Time taken = {t1 - t0}')
#findNemo(nemo) #O(n) --> Linear time

boxes = [0,1,2,3,4,5]
def logFirstTwoBoxes(boxes):
    print(boxes[0]) #0(1)
    print(boxes[1]) #0(1)

logFirstTwoBoxes(boxes) #0(2)  0(1) --> Constant time