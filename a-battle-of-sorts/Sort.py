def insertion_sort(arr):
  for k in range(1, len(arr)):
    cur = arr[k]
    j = k
    while j > 0 and arr[j-1] > cur:
      arr[j] = arr[j-1]
      j = j - 1
    arr[j] = cur

a = [4,-2,8,-1]
insertion_sort(a)

def selection_sort(arr):
  for current_index in range(len(arr)):
    minimum_remaining_card_index = arr.index(min(arr[current_index,len(arr)]))
    if current_index == minimum_remaining_card_index:
      continue
    else:
      # swap cards
      alias = minimum_remaining_card_index
      minimum_remaining_card_index = arr[current_index]
      current_index = arr[alias]

a = [4,-2,8,-1]
selection_sort(a)


