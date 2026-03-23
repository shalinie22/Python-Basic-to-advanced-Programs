# 2. Timing Decorator

# 👉 Create a decorator that:

# Measures how long a function takes to execute
# Prints execution time

import time
def my_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time-start_time)

    return wrapper

@my_decorator
def say_hello():
    print("HHHHaaaaaaaaaaaiiiiiiiiiiiiiii")


say_hello()
