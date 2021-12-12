import multiprocessing
import time

start = time.perf_counter() #start time

def doSomething():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping...')


if __name__ == '__main__':

    processes = []

    for _ in range(10):
        p1 = multiprocessing.Process(target=doSomething)
        p1.start()
        processes.append(p1)

    for process in processes:
        process.join()

    end = time.perf_counter() #end time

    print(f'Finished in {round(end - start, 2)} second(s)')