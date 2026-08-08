class BankAccount:

    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):

        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount


account = BankAccount("Abhay", 5000)

print(account.owner)
print(account.balance)

account.deposit(2000)
print(account.balance)

account.withdraw(1000)
print(account.balance)

account.balance = 10000
print(account.balance)

account.balance = -500