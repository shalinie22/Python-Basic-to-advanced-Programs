# Given a list [1,2,3,4], use map() to square all elements

l = [1,2,3,4]

sqfn = list(map(lambda x:x**2, l))

print(sqfn)



# Convert a list of strings ["1","2","3"] to integers

l = ["1","2","3"]
print(list(map(lambda x: int(x), l)))

# Convert list of names to uppercase
names = ["Tae","Lee","Vincenzo"]

print(list(map(lambda x:x.upper(), names)))

# Given [10,20,30], add 5 to each element

print(list(map(lambda x:x+5, [10,20,30])))

