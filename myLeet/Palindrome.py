
class Palindrome:
    def isPalindrome(self, num):
        originalNum = num
        reversedNum = 0
        while(num > 0):
            remainder = num % 10
            reversedNum = reversedNum * 10 + remainder
            num = num // 10

        isPalin = False
        if originalNum == reversedNum:
            isPalin = True

        return isPalin

if __name__ == '__main__':
    palindrome = Palindrome()
    num = 121
    flag = palindrome.isPalindrome(num)
    print(f'{num} is palindrome {flag}')