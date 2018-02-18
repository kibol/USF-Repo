##14

from sys import argv

nums = argv[1:]

for i, value in enumerate(nums):
    nums[i] = float(value)

mean = sum(nums) / len(nums)


#16

##from sys import argv
##infile = open('alice_in_wonderland.txt', 'r')
##text = infile.read()
##infile.close()

