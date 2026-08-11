from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, user):
        self.user = user

    @abstractmethod
    def pay(self, amount):
        pass

    def receipt(self):
        print(f"Receipt generated for {self.user}")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class PayPal(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


upi = UPI("Abhay")
card = CreditCard("Rahul")

upi.pay(1000)
upi.receipt()

print()

card.pay(2000)
card.receipt()