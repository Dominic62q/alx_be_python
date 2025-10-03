class BankAccount:
    def __init__(self, account_balance=0):  # default balance is 0
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if amount <= self.account_balance:   # funds are enough
            self.account_balance -= amount
            return True                      # success
        else:
            return False                     # insufficient funds, no change

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

