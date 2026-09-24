nums = [2, 3, 6, 6, 4, 7, 8]

def sec_max(nums: list):
    # unique_nums = set(nums)
    # high_num = max(unique_nums)
    # unique_nums.remove(high_num)
    # return max(unique_nums)
    return sorted(set(nums))[-2]

print(sec_max(nums))