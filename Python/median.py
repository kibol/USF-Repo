#15
from sys import argv
nums = argv[1:]

for i, value in enumerate(nums):
    nums[i] = float(value)
    
nums.sort()
size = len(nums)
middle = size / 2

if size % 2 == 0:
    median = (nums[middle - 1] + nums[middle]) / 2
else:
    median = nums[middle]



    
    
