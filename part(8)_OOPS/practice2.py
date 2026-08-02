class Account():
    def __init__(self , balance , account_No):
        self.balance=balance
        self.account_No=account_No

    def debit(self , amount):
        self.balance-=amount
        print("Balance debitted " , amount)   
        print("total balance is " , self.get_balance()) 

    def credit(self , amount):
        self.balance+=amount
        print("Balance credited ",amount) 
        print("total balance is " , self.get_balance()) 


    def get_balance(self):
        return self.balance  

acc1=Account(12000, 5625010000688)
acc1.debit(1000)
acc1.credit(3000)   
acc1.credit(40000)   