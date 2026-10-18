# Process API Data
# Create a dictionary containing only active users,
# with id as the key and name as the value.
# {1: "John", 3: "Bob"}

users = [
    {"id": 1, "name": "John", "active": True},
    {"id": 2, "name": "Alice", "active": False},
    {"id": 3, "name": "Bob", "active": True},
]
result: dict={}
for user in users:
    if user["active"]:
        key = user["id"]
        value = user["name"]
        result[key] = value
print(result)

print({
    user["id"]: user["name"]
    for user in users
    if user["active"]
})