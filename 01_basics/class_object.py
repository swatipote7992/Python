class Receipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The"+self.dish+"has"+self.items +
              "and takes"+self.time+"to prepare")


pizza = Receipe('Pizza', ['cheese', 'chicken', 45])
pasta = Receipe('Pasta', ['cheese', 'tomota', 34])

print(pizza.items)
print(pasta.items)

# Example 2


class MyFirstClass:

    index = 'Author-Book'

    def hand_list(self, philosopher, book):
        self.philosopher = philosopher
        self.book = book
        print('Who wrote this?')
        print(self.philosopher+"wrote the book: " + self.book)


# Call function handlist()
my_class = MyFirstClass()
my_class.hand_list('Plato', 'Republic')
