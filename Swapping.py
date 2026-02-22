# swapping with temporary variable

a = 5
b = "Sha"

temp = a
a=b
b = temp

print(a,b)

#swapping without temp variable

a = "V"
b = "S"
a,b = b,a

print(a,b)