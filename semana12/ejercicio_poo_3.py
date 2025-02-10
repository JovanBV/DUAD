'''
This class represents a general bank account with an initial balance of zero.
It allows users to deposit and withdraw money, but only if the amount is a numerical value.
Negative balances are allowed.
'''

class BankAccount:
    balance = 0

    def deposit(self, amount):
        try:
            self.balance += amount
        except:
            raise ValueError("Deposit amount must be an integer.")

    def withdraw(self, amount):
        try:
            self.balance -= amount
        except:
            raise ValueError("Withdrawal amount must be an integer.")

'''
This class represents a savings account, which is a subclass of BankAccount.
Users can deposit money as usual, but withdrawals are restricted:
the account balance cannot drop below a specified minimum balance.
'''

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.account_min_balance = min_balance

    def deposit(self, amount):
        super().deposit(amount)
    
    def withdraw(self, amount):
        if self.balance - amount < self.account_min_balance:
            raise ValueError("Withdrawal denied. Account balance cannot go below the minimum required balance.")
        else:
            super().withdraw(amount)

account = SavingsAccount(10)

account.deposit(20)
account.withdraw(10)  
account.deposit(100)
account.withdraw(100)  

print(account.balance)
