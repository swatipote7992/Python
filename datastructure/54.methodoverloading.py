# method overloading
# approach 1 - default argument
class Price:
    def __init__(self, premium):
        self.premium = premium

    def calculate_premium(self, base, discount=0):
        print(base - discount)


# Now both calls work
price = Price(1000)
price.calculate_premium(1000)
# 1000

price.calculate_premium(1000, 100)
# 900


# Another approach is *args:
class Quote:
    def calculate_premium(self, *args):
        if len(args) == 1:
            return args[0]

        if len(args) == 2:
            return args[0] - args[1]

        raise ValueError("Invalid arguments")
