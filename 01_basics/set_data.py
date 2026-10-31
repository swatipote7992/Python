my_set = {}
print('Type:', type(my_set))
# Set cannot be empty

set_a = {1, 2, 3, 4, 5}
print("Set A:", set_a)
# print(set_a[0])

# Set Operations
set_a.add(6)
print('Set A after adding 6:', set_a)
set_a.remove(3)
print('Set A after removing 3:', set_a)
set_a.discard(4)  # Discarding an element that may not exist
print('Set A after discarding 4:', set_a)

# Set Merge Operations
# Union merges the duplicate values and create a new set
set_d = {1, 2, 3, 4, 5}
set_e = {1, 3, 6, 7, 8}
print('Union of d and e', set_d | set_e)
print('Interset of d and e', set_d.intersection(set_e))
print('Difference', set_d.difference(set_e))
print('Similary using minus', set_d - set_e)
print('Symmetric difference', set_d.symmetric_difference(set_e))
print('Caring Operator', set_d ^ set_e)
