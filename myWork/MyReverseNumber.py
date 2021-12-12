

def myReverse(num):

    if num == 0:
        return
    reverse = 0
    while num > 0:
        reminder = num % 10
        reverse = reverse * 10 + reminder
        num = num // 10

    return reverse


if __name__ == '__main__':
    num = myReverse(1234)
    print("Reverse number is ", num)