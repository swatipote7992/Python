# Create your own decorator that prints a message before and after a function executes.
# Expected Output
# For:
# say_hello()
# Expected:
# Before function
# Hello
# After function

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print('Hello')

say_hello()