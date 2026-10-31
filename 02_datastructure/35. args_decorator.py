# #prod style decorator with *args and *kwargs

from functools import wraps
def args_decorator(func):
    @wraps(func)
    def wrapper(*args):
        print('Before Function')
        func(*args)
        print('After Function')
    return wrapper

@args_decorator
def say_hello(*args):
    print("Hello", *args)

say_hello(1,2,3)
