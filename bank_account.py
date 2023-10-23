'''Import random module to generate random account numbers'''
import random

'''Create a Bank_Account class with the following attributes:
full_name, account_num, account_balance, account_type
'''
class Bank_Account:
    '''Create a Bank_Account class with the following attributes: full_name, account_num, account_balance, account_type'''
    def __init__(self, full_name, account_num, account_balance = 0, account_type = 'checking'):
        self.full_name = full_name
        self.account_num = account_num
        self.account_balance = account_balance
        self.account_type = account_type

    def deposit(self, amount):
        '''Add amount to account_balance'''
        self.account_balance += amount
        print(f"Amount deposited: ${amount}. New balance: ${self.account_balance}")


    def withdraw(self, amount):
        '''Subtract amount from account_balance'''
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Amount withdrawn: ${amount}. New balance: {self.account_balance}")
        else:
            self.account_balance -= 10
            print("Insufficient funds.")


    def get_balance(self):
        '''Print current account balance'''
        print(f"Welcome, {self.full_name}. Your current account balance for account number: {self.account_num} is ${self.account_balance}")
        return self.account_balance

    def add_interest(self):
        '''Add interest to account_balance based on account_type'''
        if self.account_type == 'checking':
            interest = self.account_balance * 0.00083
        elif self.account_type == 'savings':
            interest = self.account_balance * 0.01
        self.account_balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.account_balance}")

    def print_statement(self):
        '''Print account information'''
        print(f"Name: {self.full_name}")
        print(f"Account No.: ****{str(self.account_num)[4:]}")
        print(f"Balance: ${self.account_balance}\n")



# Helper function to generate random unique account number
accounts = []
def generate_account_num():
    '''Generate random account number'''
    while True:
        account_num = random.randint(10000000, 99999999)
        if account_num not in accounts:
            return account_num


new_account = generate_account_num()
new_account1 = generate_account_num()
new_account2 = generate_account_num()
new_account3 = generate_account_num()
new_account4 = generate_account_num()

marks_account = Bank_Account('Mark', new_account, 23.43)
marks_account.get_balance()
marks_account.deposit(3424)
marks_account.print_statement()
marks_account.withdraw(321)
marks_account.get_balance()
marks_account.add_interest()
marks_account.print_statement()

phils_account = Bank_Account('Phil', new_account1, 32.3)
phils_account.get_balance()
phils_account.add_interest()
phils_account.withdraw(12.2)
phils_account.print_statement()
phils_account.get_balance()


mitchells_account = Bank_Account('Mitchell', 13141592, 400000)
mitchells_account.print_statement()
mitchells_account.add_interest()
mitchells_account.print_statement()
mitchells_account.withdraw(150)
mitchells_account.print_statement()

# Stretch Challenges (also check bank.py and application.py)
mark_savings_account = Bank_Account('mark_savings', new_account2, 1000, 'savings')
mark_savings_account.add_interest()

mark_checking_account = Bank_Account('mark_checking', new_account3, 1000, 'checking')
mark_checking_account.add_interest()

mark_checking_account.print_statement()
mark_savings_account.print_statement()


bank = [mark_checking_account,
        mark_savings_account,
        mitchells_account,
        phils_account,
        marks_account]

for account in bank:
    account.add_interest()
