nums = [1, 2, 3, 2, 2, 4, 5, 1]









def remove_dup(nums):
    num_set = list(set(nums))
    return num_set


print("Removing Dup", remove_dup(nums))

# This preserves the first occurrence order
unique_numbers = list(dict.fromkeys(nums))
print(unique_numbers)





