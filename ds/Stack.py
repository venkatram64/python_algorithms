
#Stack is a LIFO(Last In First Out) data structure
from collections import deque

def addElements(nums):
    stack = deque()
    print(dir(stack))
    for i in nums:
        stack.append(i)

    print("Below one is iteration:")
    for i in stack:
        print(f'{i}')

    #poping the elements
    print("Below one is stack popping out")
    while len(stack) > 0:
        print(f'{stack.pop()} popped out...')




if __name__ == '__main__':
    addElements([3,6,8,9,2,5,7])
