
def myForEven():
    even = [x for x in range(20) if x % 2 == 0]
    print(even)

#list comprehension
def myForFromString():
    myStr = "my test 123 is fun"
    newStr = [int(x) for x in myStr if x.isdigit()]
    print(newStr)

#map comprehension
def myForWithDic():
    keys = [1, 2, 3, 4, 5]
    values = ['a', 'b', 'c', 'e', 'f']

    newDict = {k:v for (k,v) in zip(keys, values)}

    print(newDict)

def myForEvenAndDevideByFive():
    evenWithFive = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
    print(evenWithFive)

def myEvenOrOdd():
    evenOrOdd = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
    print(evenOrOdd)


if __name__ == '__main__':
    #myForFromString()
    #myForWithDic()
    #myForEven()
    #myForEvenAndDevideByFive()
    myEvenOrOdd()