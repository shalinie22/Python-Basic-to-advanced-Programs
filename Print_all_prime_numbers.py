lower = int(input("Enter the starting value:"))
upper = int(input("Enter the ending value:"))

for num in range (lower, upper+1):
    if num>1:
        for i in range(2, num):
            if(num%i==0):
                break
        else:
            print(num)