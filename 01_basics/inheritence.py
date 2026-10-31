class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))

print(issubclass(A, B))
print(issubclass(B, A))
