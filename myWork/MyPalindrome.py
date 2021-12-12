

def isPalindrom(strM):

    strM = strM.lower()
    if strM == None:
        print("String should not be none")
        return

    length = len(strM)
    newStr = ''
    for i in range(0, length):
        newStr += strM[length - i - 1]

    print("new string is ", newStr)
    if newStr == strM:
        return True
    else:
        return False


if __name__ == '__main__':
    strM = input("Enter a string to check palindrome: ")
    #strM = 'malayalam'
    flag = isPalindrom(strM)
    print("is palindrom ", flag)
