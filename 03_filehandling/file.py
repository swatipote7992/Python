# with open("names.txt", 'a') as f :
#     f.write("Neil \n")

# with open("names.txt", 'r') as f:
#     print(f.read())

# with open("names.txt", "r") as f:
#     print(f.readline())

# with open("names.txt", 'w') as f:
#     f.write('Max')

# with open("names.txt", 'r') as f:
#     print(f.read())

# with open("names.txt", 'a') as f:
#     f.write('Oliver')

# with open("names.txt", 'r') as f:
#     print(f.read())

with open("sample.txt", 'w') as f:
    print(f.write('Hello Python\nI am learning file handling\nPython is easy'))

with open("sample.txt", 'r') as f:
    content = f.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)
    print(f"Lines:{len(lines)}")
    print(f"Words:{len(words)}")
    print(f"Characs:{characters}")


# How would you read the file line by line instead of loading the entire file into memory?
linecount = 0
with open("sample.txt") as f:
    for line in f:
        linecount += 1
        print(line.strip())
    print('linecount', linecount)

