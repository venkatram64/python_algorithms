#https://www.w3schools.com/python/python_dictionaries_methods.asp
def myDectionary1():
    squares = {}
    for x in range(6):
        squares[x] = x * x

    print(squares)
    print("******************")
    return squares

if __name__ == '__main__':
    myDict = myDectionary1()

    #1.
    for key in myDict.keys():
        print(myDict.get(key))

    print("***************")

    #2.
    for key, value in myDict.items():
        print(f'{key}: {value}')