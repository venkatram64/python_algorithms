
def fibanacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibanacci(n-1) + fibanacci(n-2)


if __name__ == '__main__':
    for i in range(1, 10):
        fib = fibanacci(i)
        print(f"Fib of {i} is {fib}")