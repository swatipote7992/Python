my_tuple = (1, 'string', 3.14, True)
print("Tuple of Mixed Data Types:", my_tuple)

# Accessing elements in a tuple
print('First element:', my_tuple[0])  # Accessing first element
print('Last element:', my_tuple[-1])  # Accessing last element
print('Index of 3.14:', my_tuple.index(3.14))  # Finding index of an element

# Iterating through tuple elements
print('Iterating through tuple elements:')
for idx, item in enumerate(my_tuple):
    print(f"Index: {idx}, Value: {item}")  # Iterating through tuple elements
