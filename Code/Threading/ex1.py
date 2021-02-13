""" use of Threading module """

import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds..')
    time.sleep(seconds)
    print('Done sleeping..') 


if __name__ == '__main__':
    threads = []
    for _ in range(10):
        t = threading.Thread(target=do_something, args=[1.5])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'finished in {round(finish - start,2)} second(s)')