
#Stack is a LIFO(Last In First Out) data structure
from collections import deque

def addElements(nums):
    queue = deque() #deque can be used as queue
    print(dir(queue))
    for i in nums:
        queue.appendleft(i)

    print("Below one is iteration:")
    for i in queue:
        print(f'{i}')

    #poping the elements
    print("Below one is queue popping out")
    while len(queue) > 0:
        print(f'{queue.pop()} popped out...')




if __name__ == '__main__':
    addElements([3,6,8,9,2,5,7])
