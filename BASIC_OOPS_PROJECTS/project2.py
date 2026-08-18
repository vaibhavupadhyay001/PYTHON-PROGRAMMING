class BankException(Exception):
    pass


class BankAccount:
    def __init__(self , initialAmount , accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created. \nBalance = ${self.balance:.2f} ")

    def get_balance(self):
        print(f"Available '{self.name}' balance is:- ${self.balance:.2f}")

        print()

    def deposit(self , amout):
        self.balance = self.balance + amout
        print(f"\nDeposit complete")
        self.get_balance()

        print()

    def check(self , amount):
        if self.balance >= amount:
            return
        else:
            raise BankException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance}")

    def withdraw(self , amount):  
        try:
            self.check(amount) 
            self.balance=self.balance-amount
            print(f"Withdraw is complete.")
            self.get_balance()

        except BankException as error:
            print(f"\nWithdraw interrupted:{error}")  


            print()



    def transfer(self , amount , account):
        try:
            print(f"\n*************\nBeginnig Transfer....🚀\n")
            self.check(amount)
            self.withdraw(amount)
            account.deposit(amount)

            print('\n Trasaction completed! ✅' \
            '\n***********')

        except BankException as error:
            print(f"\n Transfer interrupted.🔴 {error}.")    


class InterestRewardsAcc(BankAccount):
    def deposit(self, amout):
        self.balance= self.balance + (amout* 1.05)
        print("\nDeposite complete")
        self.get_balance()



class SavingsAcc(InterestRewardsAcc):
    def __init__(self , initialAmount , accName):
        super().__init__(initialAmount , accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.check(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\n withdraw completed')
            self.get_balance()

        except BankException as error:
            print("\nWithdraw interrupted..")    






        
        
