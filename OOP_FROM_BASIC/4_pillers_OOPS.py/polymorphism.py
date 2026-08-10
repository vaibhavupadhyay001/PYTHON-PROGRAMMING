class CreditCard:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Cash:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


def process_payment(self, amount):
    self.pay(amount)


process_payment(CreditCard(), 1000)
process_payment(UPI(), 500)
process_payment(Cash(), 200)




class PayPal:

    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")




process_payment(PayPal(), 2000)       