
class BalanceException(Exception):
    pass



class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.get_balance()
        
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
            
    
    def transfer(self, amount, account):
        try:
            print(f"\n{'*' * 10}\n\nBeggining Transfer.. 🚀")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer complete! ✅\n\n{'*' * 10}")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")