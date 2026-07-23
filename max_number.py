# 1. Find Maximum Number

# Write a function find_max(numbers) that returns the largest element in a list without using the built-in max().

# Input:
# [10, 5, 25, 18]

# Output:
# 25



def find_maximum(nums):
    max_num = nums[0]
    for i in nums:
        if i>max_num:
            max_num = i
    return max_num

print(find_maximum([10, 5, 25, 18]))