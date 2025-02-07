class BankAccount:
    balance = 0

    def deposit(self, amount):
        try:
            self.balance += amount
        except:
            raise ValueError("Deposit amount must be an integer.")

    def withdraw(self, amount):
        try:
            if self.balance - amount < 0:
                raise ValueError("Insufficient funds. Withdrawal amount exceeds balance.")
            else:
                self.balance -= amount
        except:
            raise ValueError("Withdrawal amount must be an integer.")

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
