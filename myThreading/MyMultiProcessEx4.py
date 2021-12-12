import concurrent.futures
import time

start = time.perf_counter() #start time

def doSomething(seconds):
    print(f'Sleeping {seconds} second(s)')
    time.sleep(seconds)
    print(f'Done Sleeping...{seconds} second(s)')

def processExecutor():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(doSomething, sec) for sec in secs]
        return results

if __name__ == '__main__':

    f1 = processExecutor()
    for e in concurrent.futures.as_completed(f1):
        e.result()

    end = time.perf_counter() #end time

    print(f'Finished in {round(end - start, 2)} second(s)')