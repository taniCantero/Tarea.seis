from bank_account import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

Dave.get_balance()
Sarah.get_balance()

Dave.deposit(2000)

Dave.transfer(4000, Sarah)


Jim = InterestRewardsAccount(1000, "Jim")

Jim.get_balance()
Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(1000, Sarah)
# Blaze.withdraw(100)