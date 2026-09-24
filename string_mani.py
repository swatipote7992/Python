data_str = "Hello World"

rev_str = data_str[::-1]
print('Rev str:', rev_str)

reveresed_string = "".join(reversed(data_str))
print("reveresed_string", reveresed_string)

print('Remove spaces: ', data_str.replace(" ", ""))

print('Split words:', data_str.split())

print('Join string of array:', " ".join(['Hello', 'World']))

print("Join string of array:", "".join(["Hello", "World"]))

