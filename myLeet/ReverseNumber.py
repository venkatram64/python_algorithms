class ReverseNumber:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        reverseNum = 0
        isPositive = True
        if x < 0:
            isPositive = False
            x = - 1 * x
        while x > 0:
            remainder = x % 10
            reverseNum = reverseNum * 10 + remainder
            x = x // 10

        if not isPositive:
            reverseNum = - reverseNum

        #if reverseNum in range(-2 ** 31, (2 ** 31) - 1):
        if abs(reverseNum) < 2 ** 31 and reverseNum != 2 ** 31 - 1:
            return reverseNum
        else:
            return 0



if __name__ == '__main__':
    rn = ReverseNumber()
    num = 1534236469 #-123
    reversedNum = rn.reverse(num)
    print(f'{num} is {reversedNum}')