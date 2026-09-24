def is_palindrome(data: str):
    rev_str = data[::1]
    result = rev_str == data
    print(f'is {data} palindrome', result )

is_palindrome('madam')
is_palindrome('hello')

def is_anagram(data1: str, data2: str):
    return sorted(data1) == sorted(data2)
    
print(is_anagram('listen', 'silent'))
print(is_anagram('madam', 'hello'))





# def is_anagram(data_str1: str, data_str2: str):
#     return sorted(data_str1) == sorted(data_str2)

# print('is_anagram', is_anagram('listen', 'silent'))
# print('is_anagram', is_anagram('hello', 'world'))


# def is_palindrome(str1: str):
#     return str1 == str1[::-1]

# print('is_palindrome',is_palindrome('madam'))
# print("is_palindrome", is_palindrome("hello"))