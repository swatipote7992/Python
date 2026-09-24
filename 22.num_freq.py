# Number Frequency
# Count the frequency of each number in numbers = [1, 2, 2, 3, 3, 3, 4]
# { 1: 1, 2: 2, 3: 3, 4: 1, }








num_list = [1, 2, 2, 3, 3, 3, 4]
result2_dict: dict = {}
for num in num_list:
    result2_dict[num] = result2_dict.get(num, 0) + 1
print(result2_dict)
