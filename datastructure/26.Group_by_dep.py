# Group Users by Department
# Expected Output
# {
#     "IT": ["John", "Bob"],
#     "HR": ["Alice"],
#     "Finance": ["David"]
# }

users_list = [
    {"name": "John", "department": "IT"},
    {"name": "Alice", "department": "HR"},
    {"name": "Bob", "department": "IT"},
    {"name": "David", "department": "Finance"},
]

result_dict: dict = {}
for user in users_list:
    dept = user["department"]
    if dept not in result_dict:
        result_dict[dept] = []
    result_dict[dept].append(user["name"])

print(result_dict)