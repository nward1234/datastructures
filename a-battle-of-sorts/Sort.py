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
            swap_ind = arr.index(cur_min)
            arr[k] = cur_min
            arr[swap_ind] = cur


a = [4, -2, 8, -1]
selection_sort(a)
print(a)


# if __name__ == '__main__':
# main section here,
# within this big conditional
