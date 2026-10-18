# Example:

# nums = [5, 2, 8, 1, 3]
# target = 8
# Expected Output
# Sorted: [1, 2, 3, 5, 8]
# Found: True

def sort_search(nums: list, target: int):
    sort_num = sorted(nums)
    return target in sort_num

nums = [5, 2, 8, 1, 3]
print(sort_search(nums, 8))

#also check binary_search.py