# Find duplicate records based on a field such as id.

# Expected Output
# [
#     {"id": 1, "name": "John"},
#     {"id": 2, "name": "David"}
# ]

records = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "David"},
    {"id": 1, "name": "John"},
    {"id": 3, "name": "Sarah"},
    {"id": 2, "name": "David"}
]


def find_dup(record_list: list):
    seen = set()
    dup = []
    for record in record_list:
        if record["id"] in seen:
            dup.append(record)
        else:
            seen.add(record["id"])
    return dup

print(find_dup(records))












# def find_duplicates(records):
#     seen = set()
#     duplicates = []
#     for record in records:
#         record_id=record["id"]
#         if record_id in seen:
#             duplicates.append(record)
#         else:
#             seen.add(record_id)
#     return duplicates
# print(find_duplicates(records))


# #Group Records by Field
# # Problem

# # Group records based on a field, for example grouping employees by department.

# # Expected Output
# # {
# #     "IT": [
# #         {"name": "John", "department": "IT"},
# #         {"name": "Sarah", "department": "IT"}
# #     ],
# #     "HR": [
# #         {"name": "David", "department": "HR"}
# #     ]
# # }

# def group_by(records, field):
#     result = {}

#     for record in records:
#         key = record[field]

#         if key not in result:
#             result[key] = []

#         result[key].append(record)

#     return result


# employees = [
#     {"name": "John", "department": "IT"},
#     {"name": "David", "department": "HR"},
#     {"name": "Sarah", "department": "IT"},
# ]

# print(group_by(employees, "department"))


# # Cleaner Python Version
# # Using defaultdict:
# # from collections import defaultdict
# # def group_by(records, field):
# #     result = defaultdict(list)
# #     for record in records:
# #         result[record[field]].append(record)
# #     return dict(result)
# # Interview answer:
# # I would use a dictionary or defaultdict(list) where the field value becomes the key and each record is appended to the corresponding list.