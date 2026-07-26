# 13. Squares of Even Numbers

# Given

# numbers=[1,2,3,4,5,6]

# Return

# [4,16,36]

# using list comprehension.

def even_squares(nums):
    return [i**2 for i in nums if i%2==0]

print(even_squares([1,2,3,4,5,6]))

# 14. Remove Empty Strings

# Input

words=["apple","","orange","","grape"]

# Output

# ['apple','orange','grape']

def remove_empty(words):
    return [i for i in words if i!=""]

print(remove_empty(words))

# 15. Matrix Flattening

# Given

matrix=[
[1,2],
[3,4],
[5,6]
]

# Return

# [1,2,3,4,5,6]

def mat_flat(matrix):
    return [j for i in matrix for j in i]

print(mat_flat(matrix))

# 16. Dictionary Comprehension

# Create a dictionary

# 1:1
# 2:4
# 3:9
# ...
# 10:100

# using dictionary comprehension.

def create_dict(n):
    return {i:i*i for i in range(1,n+1)}

print(create_dict(10))