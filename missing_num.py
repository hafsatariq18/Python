# Given an unsorted array of integers, find the smallest missing positive integer.

def first_missing_positive(nums):
    n = len(nums)
    
    # Step 1: Place each number in its correct position if possible
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap elements
    
    # Step 2: Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1  # The missing number
    
    return n + 1  # If all numbers are in place, return next positive integer

# Input from the user
nums = list(map(int, input().split()))
print(first_missing_positive(nums))
