# Advanced
# - Q11. Find the top K most frequent words in a paragraph.
import collections

sentence = "python java python javascript java python"
exp_out = ["python", "java", "javascript"]

result = collections.Counter(sentence.split())
print(result)
print(list(result))

# to sort in top k 
k=3
print([word for word, count in result.most_common(k)])
# - Q12. Check whether two lists contain the same elements with the same frequencies.
list1 = [1, 2, 2, 3, 4]
list2 = [2, 1, 3, 2, 4]
exp_out = True

print(collections.Counter(list1) == collections.Counter(list2))
# - Q13. Find the intersection of two arrays using Counter.
nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 2, 3, 5]
exp_out = [2, 2, 3]

int_result = collections.Counter(nums1) & collections.Counter(nums2)
print('int:', list(int_result.elements()))

# - Q14. Find the minimum number of deletions required to make two strings anagrams.
str1 = "abc"
str2 = "amnop"
exp_out=4
def min_deletions(str1, str2):
    count1 = collections.Counter(str1)
    count2 = collections.Counter(str2)

    return sum((count1 - count2).values()) + sum((count2 - count1).values())


print(min_deletions(str1, str2))
#count1 - count2 → characters to delete from the first string.
#count2 - count1 → characters to delete from the second string.
#.values() → gets the deletion counts.
#sum() → calculates total deletions.

# - Q15. Find the K most frequent characters in a string.
s = "programming"
k = 3

result = collections.Counter(s)
print('k most:', [ c for c, count in result.most_common(k)])