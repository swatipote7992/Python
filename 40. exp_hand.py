def divide_func(a, b):
    return a / b


try:
    result = divide_func(40, 0)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("Something wrong", e)
    print(e.__class__)
else:
    print("Result:", result)
finally:
    print("Done")
