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
        results = executor.map(doSomething, secs) #returns result object
        return results

if __name__ == '__main__':

    results = processExecutor()
    for result in results:
        print(result)

    end = time.perf_counter() #end time

    print(f'Finished in {round(end - start, 2)} second(s)')