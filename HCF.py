x = int(input("Enter the number:"))
y = int(input("Enter the number:"))

smaller = x if x<y else y

for i in range(1,smaller+1):
    if x%i==0 and y%i==0:
        hcf = i

print(hcf)