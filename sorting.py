import numpy as np
import time


def insert_sort(array):
    for idx in range(1, len(array)):
        while array[idx] < array[idx - 1] and idx != 0:
            temp = array[idx]
            array[idx] = array[idx - 1]
            array[idx - 1] = temp

            idx -= 1

    return array


def merge_sort(array):
    if len(array) > 1:
        mid_point = len(array) // 2

        left = array[:mid_point]
        right = array[mid_point:]

        # recursively breaks array in half
        merge_sort(left)
        merge_sort(right)

        array.clear()

        # merge
        while len(left) > 0 or len(right) > 0:
            if len(left) <= 0:
                l_num = np.infty
                r_num = right[0]
            elif len(right) <= 0:
                r_num = np.infty
                l_num = left[0]
            else:
                l_num = left[0]
                r_num = right[0]

            if l_num <= r_num:
                array.append(l_num)
                left.remove(l_num)
            else:
                array.append(r_num)
                right.remove(r_num)

    return array


if __name__ == "__main__":

    test_list = [1 * np.random.randint(0, 1000) for _ in range(1000)]
    print("Test List: ", test_list)
    print('Length of Test List: ', len(test_list))
    print("———" * 25)

    start_time = time.time()
    insert_sort(test_list)
    print("Insertion sort took: ", time.time() - start_time)

    start_time = time.time()
    merge_sort(test_list)
    print("Merge sort took: ", time.time() - start_time)

    start_time = time.time()
    sorted(test_list)
    print("Python's built-in sort function took: ", time.time() - start_time)
