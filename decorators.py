# Two Types: Function (most common) and Class Decorators

# A Decorator is a function that takes another function as argument
# and extends the behavior of this function without explicitly
# modifying it
print("Basic Decorator")
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
        # must return wrapper for this to work
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

# Shows Start Alex End
print_name()

# Decorator function with arguments
print("\nDecorator with Arguments")
def start_end_decorator(func):
    # with this *args, **kwargs syntax
    # there can be as many arguments and the function will work
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        # return the addition result
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

# Shows 15
result = add5(10)
print(result)