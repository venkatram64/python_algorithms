
def factorial(num):
    if num == 0:  # base condition to come out of the recursion
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    n = 5
    fact = factorial(n)
    print(f'factorial of {n} is {fact}')