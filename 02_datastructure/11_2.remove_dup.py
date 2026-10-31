# Using set() — Simplest
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)

# Using dict.fromkeys() — Preserve Order
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)

# Using a Loop — Good for Interviews
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
seen = set()
for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print(unique_numbers)





