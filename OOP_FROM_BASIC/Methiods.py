# A function inside the class is called a method. A method is a function that is associated with an object. It is defined within the class and can access the attributes and other methods of the class.
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount): #methods

        self.balance += amount

    def withdraw(self, amount): #methods

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self): #methods

        print("Remaining Balance:", self.balance)


s1=BankAccount("Vaibhav" , 5000)
s2=BankAccount("Abhay" , 10000)

s1.deposit(2000)
s1.show_balance()

print()

s1.withdraw(1000)
s1.show_balance()

print()

s2.deposit(2000)
s2.show_balance()

print()

s2.withdraw(1000)
s2.show_balance()

