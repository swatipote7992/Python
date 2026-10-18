#######Python provides the abc module for this.
from abc import ABC, abstractmethod

class InsuranceProduct(ABC):

    @abstractmethod
    def calculate_premium(self, base):
        pass


class MotorInsurance(InsuranceProduct):
    def calculate_premium(self, base):
        return base * 1.20

#product = InsuranceProduct()
# TypeError

motor = MotorInsurance()
result = motor.calculate_premium(100)
print(result)


######Interface-like design using Protocol
from typing import Protocol


class PremiumCalculator(Protocol):
    def calculate_premium(self, base: float):
        pass

class CarInsurance:
    def calculate_premium(self, base: float) -> float:
        return base * 1.20

horse = CarInsurance()
result = horse.calculate_premium(10)
print(result)