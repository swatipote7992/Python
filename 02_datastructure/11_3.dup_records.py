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

result = []
seen = set()
for r in records:
    if r["id"] not in seen:
        seen.add(r["id"])
    else:
        result.append(r)
print(result)








# def find_dup(record_list: list):
#     seen = set()
#     dup = []
#     for record in record_list:
#         if record["id"] in seen:
#             dup.append(record)
#         else:
#             seen.add(record["id"])
#     return dup

# print(find_dup(records))
