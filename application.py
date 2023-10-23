from BankAccount import bankAccount

def application():
    print("\nWelcome to the bank!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Create an account")
        print("2. Print a statement")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. Quit")
        choice = input("Your choice: ")
        if choice == "1":
            name = input("What is your name? ")
            account_num = input("What is your account number? ")
            balance = input("What is your balance? ")
            checking_or_savings = input("Is this a checking or savings account? ")
            account = BankAccount(name, int(account_num), int(balance), checking_or_savings)
            print("Account created!")
        elif choice == "2":
            account.print_statement()
        elif choice == "3":
            amount = input("How much would you like to deposit? ")
            account.deposit(int(amount))
            print("Deposit successful!")
        elif choice == "4":
            amount = input("How much would you like to withdraw? ")
            account.withdraw(int(amount))
            print("Withdraw successful!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


application()