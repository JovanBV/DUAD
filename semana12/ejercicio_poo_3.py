'''
This class represents a general bank account with an initial balance of zero.
It allows users to deposit and withdraw money, but only if the amount is a numerical value.
Negative balances are allowed.
'''

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        try:
            amount = int(amount)
        except:
            raise ValueError("Deposit amount must be an integer.")
        
        self.balance += amount

    def withdraw(self, amount):
        try:
            amount = int(amount)
        except:
            raise ValueError("Withdrawal amount must be an integer.")
        
        self.balance -= amount

'''
This class represents a savings account, which is a subclass of BankAccount.
Users can deposit money as usual, but withdrawals are restricted:
the account balance cannot drop below a specified minimum balance.
'''

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.account_min_balance = min_balance
        BankAccount.__init__(self)

    def deposit(self, amount):
        try:
            amount = int(amount)
        except:
            raise ValueError('Deposit amount must be numerical.')
        
        super().deposit(amount)
        print(f'Deposit for {amount} completed.')

    def withdraw(self, amount):
        try:
            amount = int(amount)
        except:
            raise ValueError("Withdrawal amount must be numerical.")
        
        balance_after_withdraw = self.balance - amount
        if balance_after_withdraw < self.account_min_balance:
            raise ValueError("Withdrawal denied. Account balance cannot go below the minimum required balance.")
        else:
            super().withdraw(amount)
            print(f'Withdraw for {amount} completed')

account = SavingsAccount(10)

account.deposit(10)
account.deposit(10)
account.withdraw(10)

print(account.balance)