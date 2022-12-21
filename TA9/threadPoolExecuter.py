from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from time import sleep
import urllib.request
import numpy as np

def f1():

    def task(message):
        sleep(2)
        return message

    executor = ThreadPoolExecutor(max_workers=5)
    future = executor.submit(task, "Completed")
    print(future.done())
    sleep(3)
    print(future.done())
    print(future.result())


##########################################################################################

def f2():
    numbers = [10, 23, 54, 7, 89, 100]

    def get_max_number(list_of_nums):
        greatest_num = np.max(list_of_nums)
        sleep(2)
        print("Greatest number is :{}".format(greatest_num))

    with ThreadPoolExecutor(max_workers=4) as executor:
        thread1 = executor.submit(get_max_number, (numbers))
        print("Thread 1 executed ? :", thread1.done())
        sleep(3)
        print("Thread 1 executed ? :", thread1.done())


##########################################################################################

def f3():
    def log(n):
        log_value = np.log(n)
        sleep(1)
        return log_value

    def printbla(n):
        print(f'Bla -> {n}')

    values = [1, 10, 100, 1000]
    with ThreadPoolExecutor(max_workers=3) as executor:
        thread1 = executor.map(log, values)
    for result in thread1:
        print(np.round(result, 2))



if __name__ == '__main__':
    # f1()
    # f2()
    f3()
