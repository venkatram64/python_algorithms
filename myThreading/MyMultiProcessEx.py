import multiprocessing
import time

start = time.perf_counter() #start time

def doSomething():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping...')

p1 = multiprocessing.Process(target=doSomething)
p2 = multiprocessing.Process(target=doSomething)

if __name__ == '__main__':

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter() #end time

    print(f'Finished in {round(end - start, 2)} second(s)')