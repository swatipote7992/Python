def is_valid(s):
    stack = []

    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


example1 = "{[()]}"
print(is_valid(example1))
example2 = "{[(])}"
print(is_valid(example2))
