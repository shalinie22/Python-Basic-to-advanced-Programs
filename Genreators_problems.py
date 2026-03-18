# Write a generator to yield even numbers from 1 to 10

def even_gen():
    for i in range(1,11):
        if i%2==0:
            yield(i)

e = even_gen()
print(next(e))
print(next(e))
print(next(e))


# Write a generator for square numbers of a list
def sqnums_gen():
    for i in range(1,11):
        yield(i**2)

s = sqnums_gen()
print(next(s))
print(next(s))


# Create a generator for Fibonacci series up to n numbers

print("*********Fib series***********")

def fib(n):
    a = 0
    b = 1
    for i in range(0,4):
        yield(a)
        a=b
        b=a+b
f = fib(4)
print(next(f))
print(next(f))
print(next(f))

# Write a generator that reads a list and yields only positive numbers

print("*******Positive number**********")
l=[2,-4,5,-6,2,1,-67,3,56,-23,8,-9,2]

def pos(l):
    for i in l:
        if i>0:
            yield(i)

p = pos(l)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

# Create an infinite generator that keeps yielding numbers starting from 1

print("*****************infinite generator*************")

def infi_gen():
    i=0
    while (True):
        yield(i)
        i+=1

inf = infi_gen()

print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))
print(next(inf))