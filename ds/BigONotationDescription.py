'''
Big O notation is used to measure how running time or space
requirements for your program grow as input size grows

time = a * n + b
1. keep fastest growing term
time = a * n

2. Drop constants
time = O(n)  ===> n = number of computations

The below program is O(n) time complexity, which indicates one for loop or loop
'''

def squareIt(nums):
    squaredNumbers = []
    for n in nums:
        squaredNumbers.append(n*n)
    return squaredNumbers


if __name__ == '__main__':
    numbers = [2, 4, 9, 12, 15, 17]
    squaredNums = squareIt(numbers)

    #printing
    for n in squaredNums:
        print(n)