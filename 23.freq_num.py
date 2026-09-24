# Find the Most Frequent Number
# Find the number that appears most frequently.
# numbers = [1, 2, 2, 3, 3, 3, 4]

num_list = [1, 2, 2, 3, 3, 3, 4]
#result = 3






result_dict : dict = {}
for num in num_list:
    result_dict[num] = result_dict.get(num, 0) + 1
    final_result = max(result_dict, key=result_dict.get)
print(final_result)

# max(user_dict, key=user_dict.get) - finds the key with the highest value.