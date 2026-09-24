# Given:
# numbers = [1, 2, 3, 4, 5, 6]
# Return only the numbers that satisfy a condition.
# Expected Output
# [2, 4, 6]


def my_filter(func, nums):
    result = []
    for x in nums:
        if func(x):
            result.append(x) 
    return result

numbers = [1, 2, 3, 4, 5, 6]
print(my_filter(lambda x: x%2 == 0, numbers))