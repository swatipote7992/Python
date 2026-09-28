# Number Frequency
# Count the frequency of each number in numbers = [1, 2, 2, 3, 3, 3, 4]
# { 1: 1, 2: 2, 3: 3, 4: 1, }








num_list = [1, 2, 2, 3, 3, 3, 4]
result_dict: dict = {}
for num in num_list:
    result_dict[num] = result_dict.get(num, 0) + 1
print(result_dict)
