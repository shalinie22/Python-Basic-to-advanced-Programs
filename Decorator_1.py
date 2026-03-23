# 1. Logging Decorator

# 👉 Create a decorator that:

# Prints function name
# Prints "Execution started"
# Then runs the function


def my_decorator(func):
    def wrapper():
        print("calling: ",func.__name__)
        print("Execution started")
        func()

    return wrapper

@my_decorator
def firstfunc():
    print("first function")

firstfunc()
