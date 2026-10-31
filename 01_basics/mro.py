# Example 1
class A:
    def a(self):
        return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


class C(B, A):
    pass


# Driver code
c = C()
print(c.a())


# class A:
#     def b(self):
#         return "Function inside A"


# class B:
#     def b(self):
#         return "Function inside B"


# class C(A, B):
#     def b(self):
#         return "Function inside C"
#     pass


# class D(C):
#     pass


# d = D()
# print(d.b())

# example 3


# class A:
#     def c(self):
#         return "Function inside A"


# class B:
#     def c(self):
#         return "Function inside B"


# class C(A, B):
#     def c(self):
#         return "Function inside C"


# class D(A, C):
#     pass


# d = D()
# print(d.c)
