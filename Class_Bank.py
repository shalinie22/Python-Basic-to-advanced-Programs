# 6. Bank Account

# Create a BankAccount class with

# deposit()
# withdraw()
# check_balance()

# Prevent withdrawing more than the available balance.


class BankAccount:

    def __init__(self, total_balance):
        self.total_balance = total_balance

    def deposit(self, deposit_amt):
        if deposit_amt >0:
            self.total_balance+= deposit_amt
    
    def withdraw(self, withdraw_amt):
        if withdraw_amt <= self.total_balance:
            self.total_balance-= withdraw_amt
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(self.total_balance)

ba1 = BankAccount(50000)

ba1.check_balance()
ba1.deposit(20000)
ba1.check_balance()
ba1.withdraw(40000)
ba1.check_balance()
ba1.withdraw(40000)