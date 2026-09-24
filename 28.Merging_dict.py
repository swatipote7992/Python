# Merge Two Dictionaries
user_dict1 = {"name": "John", "age": 30}

user_dict2 = {"city": "London", "country": "UK"}

# modern python
result_dict = user_dict1 | user_dict2
print(result_dict)

# old soln
old_dict = {**user_dict1, **user_dict2}
print(old_dict)

# loop method
for key,value in user_dict2.items():
    user_dict1[key] = value
print(user_dict1)
