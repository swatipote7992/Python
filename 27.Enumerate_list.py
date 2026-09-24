# Convert List to Dictionary
# Create a dictionary where the key is the index
# and the value is the username.

users = ["John", "Alice", "Bob"]
result: dict = {}
# { 0: "John", 1: "Alice", 2: "Bob"}
for key,value in enumerate(users):
    result[key] = value
print(result)



# using comprehensions
result_dict = {
    key: value
    for key,value in enumerate(users)
}
print(result_dict)

#using explicit dict conversions
print(dict(enumerate(users)))