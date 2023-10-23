'''Import Bank_Account class from Bank_Account.py'''
from bank_account import Bank_Account
'''Import random module to generate random account numbers'''
import random


class Bank:
    '''Create a Bank class with the 'accounts' attribute'''
    def __init__(self):
        self.accounts = []


    def create_account(self, full_name, account_balance = 0, account_type='checking'):
        '''Create a new account and add it to the accounts list'''
        account_num = self.generate_account_num()
        account = Bank_Account(full_name, account_num, account_balance, account_type)
        self.accounts.append(account)
        print("Account created!")
        return account

    def deposit(self, account_num, amount):
        '''Deposit amount into provided account number'''
        account = self.find_account(account_num)
        if account:
            account.deposit(amount)
        else:
            print("Invalid account number.")

    def withdraw(self, account_num, amount):
        '''Withdraw amount from provided account number'''
        account = self.find_account(account_num)
        if account:
            account.withdraw(amount)
        else:
            print("Invalid account number.")

    def transfer(self, from_account, to_account, amount):
        '''Transfer amount from one account to another'''
        account1 = self.find_account(from_account)
        account2 = self.find_account(to_account)
        if account1 and account2:
            account1.withdraw(amount)
            account2.deposit(amount)
        else:
            print("Invalid account numbers.")

    def statement(self, account_num):
        '''Print statement for provided account number'''
        account = self.find_account(account_num)
        if account:
            account.print_statement()
        else:
            print("Invalid account number.")


    # Helper function to generate random unique account number
    def generate_account_num(self):
        '''Generate random account number'''
        while True:
            account_num = random.randint(10000000, 99999999)
            if account_num not in self.accounts:
                return account_num

    # Helper function to find an account with an account number
    def find_account(self, account_num):
        '''Find account with provided account number'''
        for account in self.accounts:
            if account.account_num == account_num:
                return account
        return None
    