# Find the first non-repeating character in a string.

s = 'swiss'
result = {}
for x in s:
    result[x] = result.get(x,0) + 1


def getkey(result):
    for key,value in result.items():
        if value == 1:
            return key
print(getkey(result))