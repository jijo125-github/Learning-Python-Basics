""" use of concurrent.futures.ThreadPoolExecutor with (list comprehension)"""

import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds..')
    time.sleep(seconds)
    return f'Done sleeping..' 


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(do_something, 2) for _ in range(10)]

        for f in concurrent.futures.as_completed(results):
            print(f.result())

    finish = time.perf_counter()
    print(f'finished in {round(finish - start,2)} second(s)')