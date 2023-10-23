import random
from bankAccount import BankAccount

class Bank:
    def __init__(self):
        self.accounts = []


    def create_account(self, full_name, account_balance = 0, account_type='checking'):
        account_num = self.generate_account_num()
        account = BankAccount(full_name, account_num, account_balance, account_type)
        self.accounts.append(account)
        print("Account created!")
        return account

    def deposit(self, account_num, amount):
        account = self.find_account(account_num)
        if account:
            account.deposit(amount)
        else:
            print("Invalid account number.")

    def withdraw(self, account_num, amount):
        account = self.find_account(account_num)
        if account:
            account.withdraw(amount)
        else: 
            print("Invalid account number.")


    def transfer(self, from_account, to_account, amount):
        account1 = self.find_account(from_account)
        account2 = self.find_account(to_account)
        if account1 and account2:
            account1.withdraw(amount)
            account2.deposit(amount)
        else:
            print("Invalid account numbers.")

    
    # Helper function to generate random unique account number
    def generate_account_num(self):
        while True:
            account_num = random.randint(10000000, 99999999)
            if account_num not in self.accounts:
                return account_num
            
    # Helper function to find an account with an account number
    def find_account(self, account_num):
        for account in self.accounts:
            if account.account_num == account_num:
                return account
        return None


# create_account() - creates a new account.

# deposit() - deposits an amount into an account with an account number

# withdraw() - removes an amount from an account with an account number

# transfer() - withdraws an amount from an account with an account number

#  and deposits the same amount to an account with another number.

# statement() - prints an statement for an account with an account number.