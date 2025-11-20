import random

nums = [random.randint(1, 20) for num in range(10)]

print(nums)
nums.sort()

def binary_search(nums, target):
  while nums:

    mid = len(nums) // 2

    if nums[mid] == target:
      return True
    elif nums[mid] > target:
      nums = nums[:mid -1]
    elif nums[mid] < target:
      nums = nums[mid+1:]

  return False

print(binary_search(nums, 5))
