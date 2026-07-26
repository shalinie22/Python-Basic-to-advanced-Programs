# 11. Filter Even Numbers

# Given

# numbers=[12,5,7,18,20,3]

# Use lambda with filter().

# Output

# [12,18,20]

def evenfilter(nums):
    return list(filter(lambda x: x%2==0, nums))

print(evenfilter([12,5,7,18,20,3]))