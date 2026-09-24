nums = [5, 2, 8, 1, 3]
target = 8


def implement(nums: list, target: int):
    data = sorted(nums)
    left_index = 0
    righ_index = len(data) - 1
    while left_index<=righ_index:
        mid_index = (left_index+righ_index)//2
        if data[mid_index] == target:
            return True
        elif data[mid_index] < target:
            left_index = mid_index+ 1
        else:
            righ_index = mid_index + 1
    return False

print(implement(nums, target))