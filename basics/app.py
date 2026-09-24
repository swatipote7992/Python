import math


print("Hello, World!")
print("This is a sample Python application.")
print("*" * 10)

# Variable Declaration
student_name = "John Doe"
student_count = 25
is_passed = True
marks = 22.3

# String Methods
course_name = "Python Programming"
print(len(course_name))  # Length of the string
print(course_name.upper())  # Convert to uppercase
print(course_name[0])  # Accessing first character
print(course_name[-1])  # Accessing last character
print(course_name[0:3])  # Splitting the string into a list
print(course_name[0:])  # Slicing the string
print(course_name[:])  # Copy of original string

# This is Comment: Escape Characters
print("This is a line with a newline character.\nThis is the second line.")
print("Python \\ is awesome!")  # Using escape character for backslash

# String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String Formatting
age = 20
print(f"{first_name} {last_name}")
print("My name is {} and I am {} years old.".format(full_name, age))

middle_name = "  William"
print(first_name.upper())  # Print the string in uppercase
print(first_name.lower())  # Print the string in lowercase
# Print the string with the first letter of each word capitalized
print(full_name.title())
# Print the string without leading and trailing whitespace
print(middle_name.rstrip())
# Find the index of the first occurrence of a substring
print(first_name.find("o"))

# Replace a substring with another substring
print(first_name.replace("o", "a"))
print(first_name.find("a"))  # Find the index of a substring that doesn't exist

print("doe" in full_name)  # Check if a substring exists in the string
# Check if a substring does not exist in the string
print("smith" not in full_name)


# Integer
count_students = 25  # Integer Declaration
avg_marks = 22.3  # Float Declaration
x = 1+2j  # complex number declaration

# Integer Methods
print(10 + 5)  # Addition 15
print(10 - 5)  # Subtraction 5
print(10 * 5)  # Multiplication 50
print(10 / 3)  # Division 3.333...
print(10 // 3)  # Floor Division 3
print(10 % 3)  # Modulus 1
print(10 ** 3)  # Exponentiation 1000


print(abs(-7))  # Absolute value 7
print(pow(2, 3))  # Power 8
print(round(3.7))  # Rounding 4
print(round(3.2))  # Rounding 3

print(max(1, 5, 3, 9, 2))  # Maximum value 9
print(min(1, 5, 3, 9, 2))  # Minimum value 1

print(int(3.7))  # Convert float to int 3
print(float(3))  # Convert int to float 3.0

x = 5
x += 3  # Increment x by 3, x becomes 8
print(x)
x -= 2  # Decrement x by 2, x becomes 6
print(x)

print(math.ceil(3.2))  # Ceiling 4
print(math.floor(3.7))  # Floor 3


# Input from user
# name = input("Enter your name: ")
# print(type(name))  # Print the type of the input
# print("Hello, " + name + "!")

# age = int(input("Enter your age: "))
# y = age + 5
# # input() function always returns a string
# # so we need to convert it to int if we want to perform arithmetic operations.
# print("In 5 years, you will be " + str(y) + " years old.")

# x = input("x: ")
# y = int(x) + 5
# print(f"x: {x}, y: {y}")

print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(None))  # False

print(bool(1))  # True
print(bool(-1))  # True
print(bool("hello"))  # True
print(bool(False))  # False
print(bool(True))  # True
print(bool("False"))  # True

# Comparison Operators
print(5 > 3)  # True
print(5 < 3)  # False
print(5 == 3)  # False
print(5 != 3)  # True
print(5 >= 3)  # True
print(5 <= 3)  # False
print(5 == "5")  # False

print(5 is 5)  # True
print(5 is not 5)  # False

print(5 is 5.0)  # False
print(5 is not 5.0)  # True

print("bag" > "apple")  # True, when sort bag comes after so its greater
print("bag" < "apple")  # False, when sort bag comes after so its not less
print("bag" == "BAG")  # False, b is 98 and B is 66 in ASCII so they are not equal

temperature = 15
if temperature > 30:
    print("Its a hot and sunny day.")
    print("Drink water.")
elif temperature > 20:
    print("Its a nice day.")
else:
    print("Its cold outside.")
print("Done.")

age = 22
if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

# Ternary Operator in Python
age = 22
message = "Eligible to vote." if age >= 18 else "Not eligible to vote."
print(message)

# and Operators
high_income = True
good_credit = False
if high_income and good_credit:
    print("and Testing - Eligible for loan.")
else:
    print("and Testing - Not eligible for loan.")


# or Operators
high_income = True
good_credit = False
if high_income or good_credit:
    print("or Testing - Eligible for loan.")
else:
    print("or Testing - Not eligible for loan.")

# not Operators
high_income = True
good_credit = False
student = True
if not student:
    print("not Testing - Eligible for loan.")
else:
    print("not Testing - Not eligible for loan.")

# comprehsive testing
high_income = True
good_credit = True
student = False
if (high_income and good_credit) and not student:
    print("comprehensive Testing - Eligible for loan.")
else:
    print("comprehensive Testing - Not eligible for loan.")

# quiz
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# for loop
for number in range(5):
    print("number:", number)

for i in range(3):
    print("Attempt", i+1, "." * (i+1))

for i in range(1, 4):
    print("Attempt", i, "." * i)

for i in range(1, 10, 2):
    print("Attempt", i, "." * i)

# nested for loop
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# while loop
number = 100
while number > 0:
    print(number)
    number //= 2

# command = "Q"
# while command != "Q":
#     command = input(">")
#     print("ECHO", command)

# Exercise to print even numbers
print("Even numbers between 1 and 10:")
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers.") 


a = 5
print(a)
del a
print(a)