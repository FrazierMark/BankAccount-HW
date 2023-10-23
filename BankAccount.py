import random

class BankAccount:
    def __init__(self, owner_name, account_num, account_balance = 0):
        self.owner_name = owner_name
        self.acct_num = account_num
        self.acct_balance = account_balance


    def deposit(self, amount):
        self.acct_balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.acct_balance}")










# Helper function to generate random unique account nuumber 
def generate_account_num():
    account = []
    while True:
        acct_num = random.randint(10000000, 99999999)
        if acct_num not in accounts:
            return acct_num