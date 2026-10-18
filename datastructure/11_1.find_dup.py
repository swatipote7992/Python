# Find Duplicate Values
# numbers = [1, 2, 3, 2, 4, 1, 5]
# result is [2, 1]










data_list = [1, 2, 3, 2, 4, 1, 5]
dup = []
seen = set()
for data in data_list:
    if data in seen:
        dup.append(data)
    else:
        seen.add(data)
print(dup)