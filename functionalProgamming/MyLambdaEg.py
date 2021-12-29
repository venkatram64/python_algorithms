#lambda
multiply = lambda x, y : x*y


prod = multiply(4,5)

print(f'Product of above numbers is {prod}')

# power function

power = lambda x, y: x ** y

p = power(2,3)
print(f'Power of above numbers is {p}')

# map

some_nums = [2, 4, 6, 8]

doubleIt = map(lambda x: x + x, some_nums)

for i in doubleIt:
    print(f'double it {i}')

strings = ["Venkkat", "Ram", "Reddy"]
cap = map(lambda x : str.upper(x), strings)

for i in cap:
    print(f'in capitals {i}')

#sorted

attendance = [35, 39, 32, 37, 30, 33]
sortedNums = sorted(attendance)  #gives new sorted list

for n in sortedNums:
    print(n)

print("****************")
#sort will modifies the list of numbers
attendance.sort(reverse=True)

for n in attendance:
    print(n)

#applying lambda for sort function

print("Applying lambda into sort function")
attendance = [35, 39, 32, 37, 30, 33]

attendance.sort(key=lambda x: x**2)

for n in attendance:
    print(n)

#tuples

class_attendance = [('4A',35), ('4B',39), ('4C',32), ('4D',37), ('4E',30), ('5F',33)]

sorted_ca = sorted(class_attendance, key=lambda x:x[1])
print(sorted_ca)

#filter

attendance = [36, 35, 39, 32, 37, 30, 33]

aboveAvgAtt = filter(lambda x: x > 35, attendance)
print("Above average attendance ", list(aboveAvgAtt))

countries = ["India", "US", "UK", "France", "Germany", "UAE"]

lengthGreaterThan3 = filter(lambda x: len(x) > 3, countries)
print(list(lengthGreaterThan3))

#reduce function will give single output

from functools import reduce

nums = [10, 14, 78, 93, 12, 76]
sum = reduce(lambda x, y: x+y, nums)

print(f"Sum is {sum}")

#max value

nums = [10, 14, 78, 93, 12, 76]
max_value = max(nums)
print(f"Max value is {max_value}")

#another way
max_value = reduce(lambda x, y: max(x, y), nums)

print(f"Max value is {max_value}")

#if else, finding max value

maxValue = reduce(lambda x, y: x if x > y else y, nums)
print(f"Max value is {maxValue}")


#nested list
scores = [[1,35,80],[2,32,75],[3,30,82],[4,33,75],[5,37,60]]
aboveAvg = 35

newMarks = map(lambda x: x[2] + 2 if x[1] >= aboveAvg else x[2] - 2, scores)

print(f"Modified scores{list(newMarks)}")

#lambda with dictionaries
sales = [{'country': 'India', 'sale':150.5}, {'country': 'China', 'sale': 200.2},{'country':'US','sale':1023}, {'country':'Uk','sale':223}]

country_key = map(lambda x: x['country'], sales)
print(f"Countries are {list(country_key)}")

sales_key = map(lambda x: x['sale'], sales)
print(f'Sales are {list(sales_key)}')

