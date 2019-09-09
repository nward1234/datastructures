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

a = [4, -2, 8, -1]

def increasing_populate(cell_num):
    increasing = []
    for k in range(cell_num):
        increasing.append(k)
    return increasing

def decreasing_populate(cell_num):
    decreasing = []
    for k in range(cell_num, 0, -1):
        decreasing.append(k)
    return decreasing

print(increasing_populate(40))
print(decreasing_populate(40))

# if __name__ == '__main__':
#   start = time.process_time()
#   insertion_sort(increasing)
#   print('Ten Thousand Increasing Insertion: ' + '{:.6f}'.format(end-start))
#   insertion_sort(decreasing)
#   insertion_sort(random)
#   end = time.process_time() 
#   start = time.process_time()
#   selection_sort(a)
#   selection_sort(increasing)
#   selection_sort(decreasing)
#   selection_sort(random)
#   end = time.process_time() 

#   start = time.process_time()
#   insertion_sort(a)
#   end = time.process_time()
