import math
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor, as_completed
import math
import time

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n% i == 0:
            return False

    return True

def byUsingProcessPool(primes):
    with ProcessPoolExecutor() as executor:
        return [(number, prime) for number, prime in zip(primes, executor.map(isPrime, primes))]

def byUsingThreadPool(primes):
    with ThreadPoolExecutor() as executor:
        return [(number, prime) for number, prime in zip(primes, executor.map(isPrime, primes))]

def byUsingWithOutThread(primes):
    return[(number,prime) for number, prime in zip(primes, map(isPrime, primes))]

'''
6643838879,
119218851371,
5600748293801,
688846502588399,
32361122672259149,
99194853094755497,
618970019642690137449562111,
1066340417491710595814572169,
19134702400093278081449423917,
162259276829213363391578010288127,
170141183460469231731687303715884105727
'''

if __name__ == '__main__':
    PRIMES = [
        6643838879,
        119218851371,
        5600748293801,
        688846502588399,
        32361122672259149,
        99194853094755497
    ]

    start = time.perf_counter()
    result = byUsingWithOutThread(PRIMES)
    for number, prime in result:
        print(f'{number} is prime {prime}')
    end = time.perf_counter()
    print(f'Time taken by no thread {end - start}')

    start = time.perf_counter()
    result = byUsingProcessPool(PRIMES)
    for number, prime in result:
        print(f'{number} is prime {prime}')
    end = time.perf_counter()
    print(f'Time taken by Process Pool {end-start}')

    start = time.perf_counter()
    result = byUsingThreadPool(PRIMES)
    for number,prime in result:
        print(f'{number} is prime {prime}')
    end = time.perf_counter()
    print(f'Time taken by Thread Pool {end - start}')

