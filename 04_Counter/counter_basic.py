# Beginner
# - Q1. Count the frequency of each character in a string.
data_str = "programming"
exp_out = { 'p': 1, 'r':2, 'o':1}

def freq_counter(data: str):
    result = {}
    for s in data_str:
        result[s] = result.get(s, 0) + 1
    return result


print(freq_counter(data_str))

import collections


def collection_counter(data: str):
    return dict(collections.Counter(data))


print(collection_counter(data_str))
# time complexity of this solution? -1
# Time complexity: O(n) – Counter iterates through each character once.
# Space complexity: O(k) – where k is the number of unique characters.


# - Q2. Count the frequency of each word in a sentence.
import collections

sentence = "python is great and python is powerful"
exp_out = {"python": 2, "is": 2, "great": 1, "and": 1, "powerful": 1}


def word_freq(sentence: str):
    return dict(collections.Counter(sentence.split()))


print(word_freq(sentence))
# Time complexity: O(n) – processes each word once (more precisely, proportional to total characters).
# Space complexity: O(k) – where k is the number of unique words.

# - Q3. Find the most frequently occurring element in a list.
import collections

data_list = [1, 2, 3, 2, 4, 2, 3, 3, 3]
exp_out = 3


def freq_num(data_list: list):
    result = collections.Counter(data_list)
    print(result)
    print(max(result, key=result.get))
    print(result.most_common(1)[0][0])


freq_num(data_list)
# most_common(1) returns the most frequent element and its count.
# [0][0] extracts the element

# - Q4. Find all elements that appear more than once.
import collections

data_list = [1, 2, 3, 2, 4, 2, 3, 3, 3, 5]
exp_out = [2, 3]


def num_count(data_list: list):
    result = dict(collections.Counter(data_list))
    result_list = []
    for k, v in result.items():
        if v > 1:
            result_list.append(k)
    print("num_count:", result_list)


num_count(data_list)


# using comprehensions
def num_countcomp(data_list: list):
    print([k for k, v in dict(collections.Counter(data_list)).items() if v > 1])


num_countcomp(data_list)

# - Q5. Find the element with the lowest frequency.
import collections

data_list = [1, 2, 3, 2, 4, 2, 3, 3, 3, 5]
exp_out = 2


def min_freq(data_list: list):
    result = dict(collections.Counter(data_list))
    return "min_freq:", min(result, key=result.get)


print("min_freq:", min_freq(data_list))
# Your expected output should be 1 (or 4 or 5),
# because all three appear once. Python returns 1 because it appears first.
# How would you return all elements with the lowest frequency, rather than just one?


def min_freq_all(data_list: list):
    result = collections.Counter(data_list)
    min_value = min(result.values())
    return [k for k, v in result.items() if v == min_value]


print(min_freq_all(data_list))