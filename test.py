# nums = [5, 2, 8, 1, 3]
# target = 8


# def implement(nums: list, target: int):
#     data = sorted(nums)
#     left_index = 0
#     righ_index = len(data) - 1
#     while left_index<=righ_index:
#         mid_index = (left_index+righ_index)//2
#         if data[mid_index] == target:
#             return True
#         elif data[mid_index] < target:
#             left_index = mid_index+ 1
#         else:
#             righ_index = mid_index + 1
#     return False

# print(implement(nums, target))


from abc import ABC, abstractmethod


class ProcessPayment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        print("hello")


class CardPayment(ProcessPayment):
    def process_payment(self, amount):
        print(f"{amount} Paid")


class BankAccount:
    account_type = "Current"

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdrw(self, amt):
        self.__balance -= amt

    def get_balance(self):
        return self.__balance

    @classmethod
    def get_acctype(cls):
        return cls.account_type


bk = BankAccount(1000)
bk.deposit(100)
bk.withdrw(50)
bal_pending = bk.get_balance()
print(bal_pending)
print(bk.account_type)

pay = CardPayment()
pay.process_payment(bal_pending)


class Vehicle:
    def cal_pre(self, base):
        return base * 10


class Audi(Vehicle):
    def cal_pre(self, base):
        baseve = super().cal_pre(base)
        return baseve + 20


audi = Audi()
print(audi.cal_pre(10))


class Quote:
    pass


class PremiumCalculator:
    def calculate(self, base):
        return base * 10


class QuoteService:
    def __init__(self, calculator):
        self.calculator = calculator

    def create_quote(self, base):
        return self.calculator.calculate(base)


calculator = PremiumCalculator()
qs = QuoteService(calculator)
print(qs.create_quote(1000))
