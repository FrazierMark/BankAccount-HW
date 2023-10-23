import random

class BankAccount:
    def __init__(self, full_name, account_num, account_balance = 0):
        self.full_name = full_name
        self.account_num = account_num
        self.account_balance = account_balance


    def deposit(self, amount):
        self.account_balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.account_balance}")


    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Amount withdrawn: ${amount}. New balance: {self.account_balance}")
        else:
            self.account_balance -= 10
            print(f"Insufficient funds.")

    def get_balance(self):
        print(f"Welcome, {self.full_name}. Your current account balance for account number: {self.account_num} is ${self.account_balance}")

    def add_interest(self):
        interest = self.account_balance * 0.00083
        self.account_balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.account_balance}")

    def print_statement(self):
        print(f"Name: {self.full_name}")
        print(f"Account No.: ****{str(self.account_num)[4:]}")
        print(f"Balance: ${self.account_balance}")


# Helper function to generate random unique account nuumber 
def generate_account_num():
    accounts = []
    while True:
        account_num = random.randint(10000000, 99999999)
        if account_num not in accounts:
            return account_num

new_account = generate_account_num()
my_new_account = BankAccount('Mark', new_account, 23.43)
my_new_account.get_balance()