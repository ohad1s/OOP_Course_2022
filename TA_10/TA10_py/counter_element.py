from concurrent.futures import ThreadPoolExecutor
from typing import List


def count_element(element: int, start: int, end: int, result: List[int]) -> int:
    count = 0
    for i in range(start, end):
        if element == result[i]:
            count += 1
    return count  # Return the count of the element

def count_element_threadpool(element: int, array: List[int], num_threads: int) -> int:
    chunk_size = len(array) // num_threads  # Size of each chunk

    # Create a thread pool
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit tasks to the thread pool
        futures = []
        for i in range(num_threads):
            start = i * chunk_size
            end = (i + 1) * chunk_size
            if i == num_threads - 1:
                end = len(array)  # Last chunk may be larger
            future = executor.submit(count_element, element, start, end, array)
            futures.append(future)

        # Wait for all tasks to complete and get the results
        count = 0
        for future in futures:
            count += future.result()  # Add the count of the element from each task

    return count

# Example usage
array = [1, 2, 3, 4,10, 6, 7, 8, 9, 10, 10, 2, 3, 4, 5, 6, 10, 8, 9, 10,10,10,10,11,0,10,10,1001,10,10]
result = count_element_threadpool(10, array, 4)
print(result)
