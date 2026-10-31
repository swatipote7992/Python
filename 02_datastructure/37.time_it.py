# Find duplicate records based on a field such as id.

# Expected Output
# [
#     {"id": 1, "name": "John"},
#     {"id": 2, "name": "David"}
# ]

from timeit import timeit

records = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "David"},
    {"id": 1, "name": "John"},
    {"id": 3, "name": "Sarah"},
    {"id": 2, "name": "David"},
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

result = find_dup(records)
time_taken = timeit(lambda: find_dup(records), number = 1000)

print("time taken is:", time_taken)

# %timeit and %%timeit are IPython magic commands — they only work in an IPython shell, Jupyter notebook, or VS Code's interactive/notebook cells. They won't work in a plain .py file run with python file.py; Python itself doesn't understand the % syntax and will raise a SyntaxError.
# %timeit — times a single line/expression:
# %timeit find_dup(records)
# It automatically figures out a good number of loops/repeats and prints something like:

# %%timeit — times an entire cell (must be the first line of the cell), useful when setup code and the code you're measuring are mixed:
# %%timeit
# records2 = [{"id": i, "name": "x"} for i in range(1000)]
# find_dup(records2)
