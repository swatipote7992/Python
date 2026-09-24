# Counting & Frequency
# Character Frequency
# Count how many times each character appears in "hello".
# result - {'h':1,'e':1,'l':2,'o':1}







text = "hello"
result_dict: dict = {}
for char in text:
    result_dict[char] = result_dict.get(char, 0) + 1
print(result_dict)
