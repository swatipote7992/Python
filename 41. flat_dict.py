# Convert a nested dictionary into a flat dictionary using dot notation.
# Given : 
data = {"user": {"name": "John", "address": {"city": "London", "postcode": "CV1"}}}

# Expected Output
# {
#     "user.name": "John",
#     "user.address.city": "London",
#     "user.address.postcode": "CV1"
# }

def flatten_dict(data_dict, parent_key="", result_dict=None) -> dict:
    result_dict = {} if result_dict is None else result_dict
    for key,value in data_dict.items():
        new_key = f"{parent_key}.{key}"
        if isinstance(value, dict):
            flatten_dict(value, new_key, result_dict)
        else:
            result_dict[new_key] = value
    return result_dict

print(flatten_dict(data))




















# def flattern_dict(data, parent_key="", result=None):
#     result = {} if result is None else result
#     for key, item in data.items():
#         new_key = f"{parent_key}.{key}" if parent_key else key
#         if isinstance(item, dict):
#             flattern_dict(item, new_key, result)
#         else:
#             result[new_key] = item
#     return result
# data = {"user": {"name": "John", "address": {"city": "London", "postcode": "CV1"}}}
# print(flattern_dict(data))