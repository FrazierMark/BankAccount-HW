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
            verify_account_num = input("What is your account number? ")
            if int(verify_account_num) == account.account_num:
                account.print_statement()
            else:
                print("Invalid account number.")

        elif choice == "3":
            verify_account_num = input("What is your account number? ")
            amount = input("How much would you like to deposit? ")
            if int(verify_account_num) == account.account_num:
                account.deposit(int(amount))
                print("Deposit successful!")
            else:
                print("Invalid account number.")
                
        elif choice == "4":
            verify_account_num = input("What is your account number? ")
            amount = input("How much would you like to withdraw? ")
            if int(verify_account_num) == account.account_num:
                account.withdraw(int(amount))
                print("Withdraw successful!")
            else:
                print("Invalid account number.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


application()