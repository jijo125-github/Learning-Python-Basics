""" use of concurrent.futures with (list comprehension)"""

import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds..')
    time.sleep(seconds)
    return f'Done sleeping..{seconds}' 


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = [executor.submit(do_something, sec) for sec in secs]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'finished in {round(finish - start,2)} second(s)')