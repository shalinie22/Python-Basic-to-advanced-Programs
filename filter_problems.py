# ilter even numbers from [1,2,3,4,5,6]

print(list(filter(lambda x:x%2==0, [1,2,3,4,5,6])))

# Filter numbers greater than 10 from a list

print(list(filter(lambda x:x>10, [23,1,4,56,7,21,22,6,4])))

# Filter strings with length > 3

print(list(filter(lambda x:len(x)>3,["Sha","Shalu","Shalinie","function"])))

# Filter positive numbers from a list with negatives

print(list(filter(lambda x:x>0, [3,-45,-2,5,-7,3,-5,1])))

# # From a list of names, filter names starting with 'A'

print(list(filter(lambda x:x.startswith("A"), ["Azure","cloud","amazon","Anaconda"])))