# Intermediate
# - Q6. Find the top 3 most frequent elements in a list.
import collections

numbers = [1, 2, 3, 2, 4, 2, 3, 3, 3, 5]
# Expected output: [3, 2, 1]

def top_thereFreq(nums: list):
    result =  collections.Counter(nums)
    return [ k for k,v in result.most_common(3)]

print(top_thereFreq(numbers))

# - Q7. Check whether two strings are anagrams.
str1 = "listen"
str2 = "silent"
exp_out = True

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram(str1, str2))

#using counter
def is_anagram_counter(str1, str2):
    return collections.Counter(str1) == collections.Counter(str2)
print(is_anagram_counter(str1, str2))

# - Q8. Find the common elements between two lists, including duplicates.
list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 3, 5]
exp_out = [2, 2, 3]

#list1.extend(list2)
combine_list = list1 + list2
print(combine_list)

def common_two(list1, list2):
    counter1 = collections.Counter(list1)
    counter2 = collections.Counter(list2)
    result = (counter1 & counter2)
    print(result)
    print(list(result.elements()))

common_two(list1, list2) 

# - Q9. Find the elements present in one list but not another.
list1 = [1, 2, 2, 3, 4, 5]
list2 = [2, 3, 5]

def intersect_list(list1, list2):
    count1 = collections.Counter(list1)
    count2 = collections.Counter(list2)
    combine_list = count1 - count2
    return list(combine_list.elements())

print('intersect_list: ', intersect_list(list1, list2))

# - Q10. Find the first non-repeating character in a string.
s = "swiss"
def non_repeat(str):
    counter_list = collections.Counter(str)

    for k,v in counter_list.items():
        if v == 1:
            return k

print(non_repeat(s))

