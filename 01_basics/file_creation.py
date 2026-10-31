# create file and write to it
def contentToWrite(name):
    return f"Hello, {name}"


message = contentToWrite("John")
file = open("output.txt", "w")
file.write(message)
file.close()


with open('names.txt', 'r') as file:
    lines = file.readlines()
print(lines)
