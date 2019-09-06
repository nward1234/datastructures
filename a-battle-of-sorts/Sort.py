# def insertion_sort(arr):
#     for k in range(1, len(arr)):
#         cur = arr[k]
#         j = k
#         while j > 0 and arr[j-1] > cur:
#             arr[j] = arr[j-1]
#             j = j - 1
#         arr[j] = cur


# a = [4, -2, 8, -1]
# insertion_sort(a)
# print("a is")
# print(a)


def selection_sort(arr):
    for k in range(len(arr)):
        cur = arr[k]
        j = k
        min_rem = arr.index(min(arr[j:-1]))
        print("min_rem is ", min_rem)
        while j < len(arr) and cur > arr[min_rem]:
          arr[j] = arr[min_rem]
          min_rem = cur


b = [4, -2, 8, -1]
selection_sort(b)
print("b is")
print(b)
