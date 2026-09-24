# Group Products
# Group the product names by category.
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Phone", "category": "Electronics"},
    {"name": "Shirt", "category": "Clothing"},
    {"name": "Jeans", "category": "Clothing"},
    {"name": "Book", "category": "Books"},
]

result_dict: dict = {}
for prod in products:
    catg = prod["category"]
    if catg not in result_dict:
        result_dict[catg] = []
    result_dict[catg].append(prod["name"])
print(result_dict)
