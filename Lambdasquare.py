# 10. Square Numbers

# Given

# nums = [2,4,6,8]

# Use lambda with map() to return squares.

# Output

# [4,16,36,64]

def square_nums(nums):
    return list(map(lambda x: x**2, nums))

print(square_nums([2,4,6,8]))