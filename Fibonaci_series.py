nterms = int(input("Enter the number of terms:"))

n1, n2 = 0, 1
count = 0

if nterms == 1:
    print(nterms)
else:
    while count<nterms:
        nth = n1+n2
        print(n1)
        n1 = n2
        n2 = nth
        count +=1
print(nth)

def fibonacci(n):
    # Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
