import time
import random


def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = cur


def selection_sort(arr):
    for k in range(len(arr)-1):
        cur = arr[k]
        j = k
        cur_min = cur
        # while loop to iterate through array in order to find the minimum
        while j < len(arr)-1:
            next_card = arr[j+1]
            if cur_min > next_card:
                cur_min = next_card
            j += 1
        # replace current card with the minimum, unless they are the same number/card
        if cur_min != cur:
            min_index = arr.index(cur_min)
            arr[k] = cur_min
            arr[min_index] = cur


def increasing_populate(cell_num):
    increasing = []
    # populates the 'increasing' array with the exact k values from 0 to the provided parameter
    for k in range(cell_num):
        increasing.append(k)
    return increasing


def decreasing_populate(cell_num):
    decreasing = []
    # populates the 'decreasing' array with the exact k values from the provided parameter down to 1
    for k in range(cell_num, 0, -1):
        decreasing.append(k)
    return decreasing


def random_populate(cell_num):
    rand_array = []
    # populates the rand_array with random values ranging from the negative (inclusive) and positive (exclusive) versions of the parameter, with the parameter's amount of values
    for k in range(cell_num):
        rand_array.append(random.randint(-cell_num, cell_num))
    return rand_array


def insertion_sort_increasing():
    start = time.process_time()
    insertion_sort(increasing_populate(1000))
    end = time.process_time()
    print('One Thousand Increasing Insertion: ' + '{:.6f}'.format(end - start))

    start = time.process_time()
    insertion_sort(increasing_populate(2500))
    end = time.process_time()
    print('Two Thousand Five Hundred Increasing Insertion: ' + '{:.6f}'.format(end - start))

    start = time.process_time()
    insertion_sort(increasing_populate(5000))
    end = time.process_time()
    print('Five Thousand Increasing Insertion: ' + '{:.6f}'.format(end - start))

    start = time.process_time()
    insertion_sort(increasing_populate(7500))
    end = time.process_time()
    print('Seven Thousand Five Hundred Increasing Insertion: ' + '{:.6f}'.format(end - start))

    start = time.process_time()
    insertion_sort(increasing_populate(10000))
    end = time.process_time()
    print('Ten Thousand Increasing Insertion: ' + '{:.6f}'.format(end - start))


def selection_sort_increasing():
    start = time.process_time()
    selection_sort(increasing_populate(1000))
    end = time.process_time()
    print('One Thousand Increasing Selection: ' + '{:.6f}'.format(end-start))

    start = time.process_time()
    selection_sort(increasing_populate(2500))
    end = time.process_time()
    print('Two Thousand Five Hundred Increasing Selection: ' + '{:.6f}'.format(end-start))

    start = time.process_time()
    selection_sort(increasing_populate(5000))
    end = time.process_time()
    print('Five Thousand Increasing Selection: ' + '{:.6f}'.format(end-start))

    start = time.process_time()
    selection_sort(increasing_populate(7500))
    end = time.process_time()
    print('Seven Thousand Five Hundred Increasing Selection: ' + '{:.6f}'.format(end - start))

    start = time.process_time()
    selection_sort(increasing_populate(10000))
    end = time.process_time()
    print('Ten Thousand Increasing Selection: ' + '{:.6f}'.format(end - start))


if __name__ == '__main__':
    insertion_sort_increasing()
    selection_sort_increasing()
