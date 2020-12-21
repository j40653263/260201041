def get_evens(nums):
    if len(nums) == 0:
        return 0
    else:
        count = get_evens(nums[1:])
        if nums[0] % 2 == 0:
            return count + 1
        else:
            return count
        
        """
        if nums[0] % 2 == 0:
          return 1 + get_evens(nums[1:])
        else:
          return 0 + get_evens(nums[1:])
        """
        
print(get_evens([0, 1, 2, 3, 4, 5]))