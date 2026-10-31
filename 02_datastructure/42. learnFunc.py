# def recursion(num):
#     print(num)
#     next = num - 3
#     if next > 1:
#         recursion(next)


# recursion(11)

def d():
    color = "green"

    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"


color = "blue"
d()

print('-----------------------------------')
num = 9

class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num


class Bike():
    num = 11


cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
Car.num = 2
print(num)

print("-----------------------------------")
class A:
    def a(self):
        return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


class C:
    pass


class D(C, B, A):
    pass


d = D()
print(d.a())
print(D.mro())
