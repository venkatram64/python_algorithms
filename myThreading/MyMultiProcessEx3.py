import multiprocessing
import time

start = time.perf_counter() #start time

def doSomething(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print('Done Sleeping...')


if __name__ == '__main__':

    processes = []

    for _ in range(10):
        p1 = multiprocessing.Process(target=doSomething, args=[1.5])
        p1.start()
        processes.append(p1)

    for process in processes:
        process.join()

    end = time.perf_counter() #end time

    print(f'Finished in {round(end - start, 2)} second(s)')