# Find the User With the Highest Score
# Exp op - Alice
user_dict = {"John": 85, "Alice": 92, "Bob": 78}

print(user_dict)
high_score = 0
result = ""
for key,value in user_dict.items():
    if value > high_score:
        result = key
        high_score = value
print(result)


##using max
highscore_user = max(user_dict, key=user_dict.get)
print(highscore_user)

# max - finds the key with the highest value.
max_score = 0
result_key = ""
result_dict = {}
for key, value in user_dict.items():
    if value > max_score:
        max_score = value
        result_key = key
result_dict[result_key] = max_score
print(result_dict)