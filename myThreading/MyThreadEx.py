import time

start = time.perf_counter() #start time

def doSomething():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping...')

doSomething()
doSomething()

end = time.perf_counter()

print(f'Finished in {round(end - start, 2)} second(s)')