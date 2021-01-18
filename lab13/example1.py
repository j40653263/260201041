def sort(lst):
    sort_helper(lst, 0, len(lst) - 1) 

def sort_helper(lst, low, high):
  if low < high:
    index_of_min = low
    min = lst[low]
    for i in range(low + 1, high + 1):
      if lst[i] < min:
        min = lst[i]
        index_of_min = i

    lst[index_of_min] = lst[low]
    lst[low] = min

    sort_helper(lst, low + 1, high)

def main():
  lst = [3, 2, 1, 5, 9, 0]
  sort(lst)
  print(lst)

main()
