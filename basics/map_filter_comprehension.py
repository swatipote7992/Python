menu = ["espresso", "matcha", "latte", "cappuccino", "cortado", "americano"]


def find_coffe(coffee):
    if (coffee[0]) == 'c':
        return coffee


# map will take find_coffee function as an argument
# and pass items from menu one by one
map_coffee = map(find_coffe, menu)
print(map_coffee)
for x in map_coffee:
    if x is not None:
        print(x)


# now lets use filter function
filter_copy = filter(find_coffe, menu)
print(filter_copy)
for x in filter_copy:
    print(x)

# using comprehension


def square(num):
    return num * 2


data = [1, 2, 3]
newData = [x+3 for x in data]
print('newdata', newData)

a = [[96], [69]]
print("".join(list(map(str, a))))

# test
numbers = [15, 30, 47, 82, 95]


def lesser(numbers):
    return numbers < 50


small = list(filter(lesser, numbers))
print(small)
