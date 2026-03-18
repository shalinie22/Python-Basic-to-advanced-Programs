# (Hint: use from functools import reduce)

from functools import reduce

# Find sum of all elements in [1,2,3,4]

print(reduce(lambda x,y: x+y,[1,2,3,4]))

# Find product of list elements

print(reduce(lambda x,y:x*y,[1,2,3,4]))

# Find maximum element in a list

print(reduce(lambda x,y:x if x>y else y,[1,2,3,4,6,5]))

# Concatenate list of strings ["a","b","c"] → "abc"

print(reduce(lambda x,y:x+y, ["a","b","c"]))

# Find sum of squares of list elements using reduce()

print(reduce(lambda x,y:x+y**2,[1,2,3,4]))