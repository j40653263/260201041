def binary_search(arr, x, low, high):

  if high >= low:
    mid = low + high // 2

    if arr[mid] == x:
      return mid
    
    elif arr[mid] < x:
      return binary_search(arr, x, mid+1, high)

    else:
      return binary_search(arr, x, low, mid-1)

  else:
    return -1

nums= [2,3,4,15,40,110,200] 
print(binary_search(nums, 15, 0, len(nums)-1))