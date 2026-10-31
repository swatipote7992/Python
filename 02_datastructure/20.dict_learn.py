my_dict: dict ={}
print('Empty dict', my_dict)

#Its Mutuable
my_dict = {1: "Test", 2: "Home", "Name": "John"}
print("Added Data,my_dict:", my_dict)

# Iterate through Dictionary
for key, value in my_dict.items():
    print(f"Key: {key} , value: {value}")

# Create a dictionary for a person:
# name = "Alice"
# age = 30
# city = "London"

user_dict = { "name": "Alice", "age": 30, "city": "London"}
print(user_dict)

# Access dictionary values
# Print - Alice, 30, London
print(user_dict["name"])  ## Direct access
print(user_dict["age"])
print(user_dict.get("city"))  # Safe access

#Add a New Key
#Add country: "UK" 

user_dict["country"] = "UK"
print(user_dict)

#Update a Dictionary Value
#Update the user's age from 30 to 31
user_dict["age"] = 31
print(user_dict)

# Check Whether a Key Exists
# Check whether "email" exists

if "email" in user_dict:
    print('exists')
else:
    print('not_exits')  # if key in user_dict:

# Loop Through a Dictionary
# Print every key and value.


for key,value in user_dict.items():
    print(f"Key:{key} and value is: {value}")

# just remember - returns the key and value together.
print(user_dict.items())



