# Create a dictionary where the key is the username
# and the value is the length of the username
# result = {"John": 4, "Alice": 5, "Bob": 3 }

users_list = ["John", "Alice", "Bob"]
result_dict = {}
for user in users_list:
    result_dict[user] = len(user)
print(result_dict)


result = {
    user: len(user)
    for user in users_list
}
print(result)