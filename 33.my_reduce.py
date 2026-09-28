# Given:
# numbers = [1, 2, 3, 4]
# Calculate the cumulative result:
# 1 × 2 × 3 × 4 = 24
# Expected Output
# 24

def my_reduce(func, nums: list) -> int:
    result = nums[0]
    for x in nums[1:]:
        result = func(result, x)
    return result

numbers = [1, 2, 3, 4]
print(my_reduce(lambda x, y: x * y, numbers))