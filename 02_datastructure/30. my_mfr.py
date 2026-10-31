# map() and filter() are built into Python, while reduce() is available from the functools module.
from functools import reduce

numbers = [1, 2, 3, 4]
print('squares', list(map(lambda x: x*x, numbers)))

print('even numbers', list(filter(lambda x: x %2 ==0, numbers)))

print('Sum all', reduce(lambda x,y: x+y, numbers))

data = [2,4, 1, 5, 3, 7, 9, 8]
print("sorted: ", sorted(data))