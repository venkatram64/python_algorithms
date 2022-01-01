#Python List can be used as Stack
def numsList(nums):

    print(f'element is {nums.pop()}')
    print(f'element is {nums.pop()}')
    print(f'element is {nums.pop()}')


if __name__ == '__main__':
    numsList([1,5,6,8,9,4])
