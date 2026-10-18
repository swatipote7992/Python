list1 = [1, 2, 3, 4, 5]
print("List of Numbers:", list1)

list2 = ["A", "B", "C", "D", "E"]
print("List of string Data Types:", list2)

list3 = ["Hello", 1, 3, True, "B", 3.14]
print("List of Mixed Data Types:", list3)

list4 = [1, 2, [3, 4], 5]
print('Nested list', list4)

data_list = [1,2,3,4,5]

# Access List

## Find first element
print('First Element: ', data_list[0])

## Find Last element
print("Last Element: ", data_list[-1])

## display without separated - 1 2 3 4 5
print('Display as string: ', *data_list)

## Comma separated array
print(data_list, sep=" ")


# Manipulate list
## Insert 10 at index 2
data_list.insert(2,10)
print("Insert 10 at index 2:", data_list)

## Length of list
print('Length of list:', len(data_list))

## Append list with 3
data_list.append(3)
print("List after appending 3:", data_list)

## Count of element 3 in list
print("Count of element 3:", data_list.count(3))

##Merge data_list_list with another list - [6, 7, 8]
data_list.extend([6, 7, 8])
print('List after extending with [6, 7, 8]:',data_list)

# Removing first occurrence of element 3
data_list.remove(3)
print("List after removing 3:", data_list)

# Removing last element
data_list.pop() 
print('List after popping last element:', data_list)

# Deleting first element
del data_list[0]  
print('List after deleting first element:', data_list)

# del by range
del data_list[1:4]
print('List after deleting values from 1 to 4:', data_list)


#Iterating through list elements:
for num in data_list:
    print(num, end=" ")
# without end , list will be displayed vertically
