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


def create_testing_arrays():
    increasing_arrays = []
    decreasing_arrays = []
    random_arrays = []
    # Organize all the 15 arrays into higher-level arrays by type of array, then put those 3 arrays (since there are 3 types) into 1 array containing them
    for k in [1000, 2500, 5000, 7500, 10000]:
        increasing_arrays.append(increasing_populate(k))
        decreasing_arrays.append(decreasing_populate(k))
        random_arrays.append(random_populate(k))
    return [increasing_arrays, decreasing_arrays, random_arrays]


def test_sorting_times(sorting_method):
    # Sets up string interpolation
    array_type_names = ['Increasing', 'Decreasing', 'Random']
    if sorting_method == insertion_sort:
        sorting_method_name = 'Insertion'
    if sorting_method == selection_sort:
        sorting_method_name = 'Selection'
    # for each array_type(incr/dec/rand), find the time it takes to be sorted
    for array_type in range(3):
        for k in range(5):
            start = time.process_time()
            sorting_method(testing_arrays[array_type][k])
            end = time.process_time()
            # Sets up cell number in string interpolation
            if k == 0:
                k = 1000
            else:
                k *= 2500
            print(
                f'{k} Cells {array_type_names[array_type]} {sorting_method_name}: ' + '{:.6f}'.format(end-start))


if __name__ == '__main__':
    testing_arrays = create_testing_arrays()

    test_sorting_times(insertion_sort)
    test_sorting_times(selection_sort)
