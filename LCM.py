x = int(input("Enter the number:"))
y = int(input("Enter the number:"))

greater = x if x>y else y

while True:
    if greater%x==0 and greater%y==0:
        lcm = greater
        break
    greater+=1

print(lcm)