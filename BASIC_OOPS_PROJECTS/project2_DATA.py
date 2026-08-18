from project2 import *
dave = BankAccount(1000 , "Dave")
sara = BankAccount(4000 , "Sara")


dave.get_balance()
sara.get_balance()

dave.deposit(1000)
sara.deposit(3000)

dave.withdraw(300)
sara.withdraw(600)


sara.transfer(200 , dave)
dave.transfer(285 , sara)


jim = InterestRewardsAcc(1000 , "JIM")
jim.get_balance()
jim.deposit(100)
jim.transfer(100, dave)



blaze=SavingsAcc(2500 , "Blaze")
blaze.get_balance()
blaze.deposit(100)
blaze.transfer(1200 , sara)