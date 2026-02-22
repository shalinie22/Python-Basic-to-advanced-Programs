f=0
num = int(input("Enter the number:"))
if num==1:
    print(num," not a prime number")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            f=1
            break

print(f"{num} is not a prime number" if f else f"{num} is a prime number")
