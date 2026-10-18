def my_map(func, items) -> list:
    result = []
    for item in items:
        result.append(func(item))
    return result

items = [1,2,3,4]
print(my_map(lambda x: x*x, items))