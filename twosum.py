nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []

def two_sum_dict(nums,target):
    seen = {}
    for key,item in enumerate(nums):
        complement = target - item
        if complement in seen:
            return seen[complement], key
        seen[item]= key
    return []

print(two_sum(nums, target))
print(two_sum_dict(nums,target))