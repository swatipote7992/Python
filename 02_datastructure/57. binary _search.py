# simple way - sort_search.py
def binary_search(given_nums,target):
    nums = sorted(given_nums)
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) //2 
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

nums = [1,2,3,5,8]
print(binary_search(nums, 8))