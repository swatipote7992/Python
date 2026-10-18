# Create a custom generator that yields 
# numbers one at a time instead of returning
# the entire list.
# Expected Output
# 1
# 2
# 3
# 4
# 5


def my_generator(nums):
    for n in range(1, nums + 1):
        yield n


for i in my_generator(5):
    print(i)


for i in my_generator(7):
    print(i)



















# def my_generator(n):
#     for i in range(1,n+1):
#         yield i

# for num in my_generator(5):
#     print(num)