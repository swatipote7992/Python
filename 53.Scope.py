# local scope
def calculate_price():
    price = 100
    print('local scope price:', price)

#print(price) - it will give NameError
calculate_price()

#global scope
base_price = 50
def total_price():
    price = 100
    total_price = base_price + price
    print('total_price:', total_price)

total_price()

# Modifying a Global Variable
count = 0
total = 20
def increment():
    global count
    count += 1
    total = 10 #local variable
    print('total:', total)


increment()
print('count:', count)

#LEGB Rule
x = "global"
def outer():
    #x = "enclosing"
    def inner():
        #x = "local"
        print(x)
    inner()


outer()

# enclosing scope
def process_quote():
    quote_status = "Calculating"  # Enclosing variable
    def calculate_premium():
        print(quote_status)
    calculate_premium()


process_quote()


# global vs nonlocal
max = 10


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

        global max
        max += 1

    inner()
    print("count", count)
    print(max)


outer()  # 1



class Quote:
    company = "ABC Insurance"

    def __init__(self, premium):
        self.premium = premium

    def get_premium(self):
        return self.premium  # self → instance

    @classmethod
    def get_company(cls):
        return cls.company  # cls → class

    @staticmethod
    def calculate_tax(amount):
        return amount * 0.2  # neither self nor cls