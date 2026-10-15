# Qi

# This can be solved via binary search




print(binary_search([0, 1, 2, 4, 6, 8, 10], 100))

def search(nums, target):

  # This can definitely be solved via binary search

  # Solution 1
  # try:
  #   return nums.index(target)
  # except ValueError:
  #   return -1

  try:
    pivot_index = None
    for i in range(1, len(nums) - 1):
      if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
        pivot_index = i
  except:
    pass

    

# Solution 1

def search(nums, target):

  # This can definitely be solved via binary search, and I am out of practice on DSA

  Solution 1
  try:
    return nums.index(target)
  except ValueError:
    return -1


# Solution 2

def binary_search(nums, target):

  start_index = 0
  end_index = len(nums)
  mid_index = (end_index + start_index) // 2

  while end_index > start_index:

    if nums[mid_index] < target:
      start_index = mid_index
    elif nums[mid_index] > target:
      end_index = mid_index
    
    mid_index = (end_index + start_index) // 2

  return mid_index

def search(nums, target):

  # This can definitely be solved via binary search

  # Approach:
    '''
    Find the pivot point and do the binary search on both sides of it
    '''

  try:
    pivot_index = None
    for i in range(1, len(nums) - 1):
      if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
        pivot_index = i
  except:
    pass


