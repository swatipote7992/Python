# Filter a Dictionary
# Create a new dictionary containing only users with scores greater than 80.
user_dict = {"John": 85, "Alice": 92, "Bob": 70, "David": 95}

result_dict = {}
for key,value in user_dict.items():
    if value > 80:
        result_dict[key] = value
print(result_dict)


# using comprehension
comp_dict = {
    key: value
    for key,value in user_dict.items()
    if value > 80
}
print(comp_dict)

print(user_dict.keys())
print(user_dict.values())