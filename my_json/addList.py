from datetime import datetime

def myAdder():

    for d in range(1, 10): #this for loop simulates the days like running 10 days
        myList = []
        for x in range(0, 24): #this for loop simulates the hours ie 24 hours
            myList.append(x)

        sum = 0
        # this simulates the hourly count is placed in myList array object, after running 24 hours
        # summing  below
        for y in myList:
            sum += y
        print("day is ", d)
        print("sum is ", sum)


if __name__ == "__main__":
    myAdder()

