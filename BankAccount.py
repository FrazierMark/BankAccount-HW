import random

class BankAccount:
    def __init__(self, owner_name, account_num, account_balance = 0):
        self.owner_name = owner_name
        self.acct_num = account_num
        self.acct_balance = account_balance


    def deposit(self, amount):
        self.acct_balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.acct_balance}")


    def withdraw(self, amount):
        if self.acct_balance >= amount:
            self.acct_balance -= amount
            print(f"Amount withdrawn: ${amount}. New balance: {self.acct_balance}")
        else:
            self.acct_balance -= 10
            print(f"Insufficient funds.")

    def get_balance(self):
        print(f"Welcome, {self.owner_name}. Your current account balance for account number: {self.acct_num} is ${self.acct_balance}")



# Helper function to generate random unique account nuumber 
def generate_account_num():
    accounts = []
    while True:
        acct_num = random.randint(10000000, 99999999)
        if acct_num not in accounts:
            return acct_num

new_account = generate_account_num()
my_new_account = BankAccount('Mark', new_account, 23.43)
my_new_account.get_balance()