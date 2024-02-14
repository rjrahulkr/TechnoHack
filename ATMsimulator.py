import datetime
import logging

# Setup logging
logging.basicConfig(filename='atm.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Account:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.transactions = []

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append((datetime.datetime.now(), 'Deposit', amount))
        logging.info(f"{self.name} deposited {amount}. New balance is {self.balance}")
        return f"Deposited {amount}. New balance is {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append((datetime.datetime.now(), 'Withdrawal', amount))
            logging.info(f"{self.name} withdrew {amount}. New balance is {self.balance}")
            return f"Withdrew {amount}. New balance is {self.balance}"
        else:
            return "Insufficient funds"

    def get_transactions(self):
        return self.transactions


class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_account = None

    def create_account(self, name, pin):
        if name in self.accounts:
            return "Account with this name already exists"
        else:
            self.accounts[name] = Account(name, pin)
            logging.info(f"New account created for {name}")
            return "Account created successfully"

    def authenticate(self, name, pin):
        if name in self.accounts:
            account = self.accounts[name]
            if account.check_pin(pin):
                self.current_account = account
                return True
        return False

    def check_balance(self):
        return self.current_account.check_balance()

    def deposit(self, amount):
        return self.current_account.deposit(amount)

    def withdraw(self, amount):
        return self.current_account.withdraw(amount)

    def get_transactions(self):
        return self.current_account.get_transactions()


# Create an instance of ATM
atm = ATM()

# Main program loop
while True:
    print("\nSelect operation:")
    print("1. Create Account")
    print("2. Authenticate")
    print("3. Check Balance")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. View Transactions")
    print("0. Exit")

    choice = input("Enter choice (0-6): ")

    if choice == '0':
        print("Exiting the ATM.")
        break

    if choice == '1':
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        print(atm.create_account(name, pin))

    elif choice == '2':
        name = input("Enter your name: ")
        pin = input("Enter your PIN: ")
        if atm.authenticate(name, pin):
            print("Authentication successful.")
        else:
            print("Authentication failed. Please check your name and PIN.")

    elif choice in ('3', '4', '5', '6'):
        if not atm.current_account:
            print("Please authenticate first.")
            continue

        if choice == '3':
            print("Your balance is:", atm.check_balance())

        elif choice == '4':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))

        elif choice == '5':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))

        elif choice == '6':
            transactions = atm.get_transactions()
            if transactions:
                print("Transaction history:")
                for transaction in transactions:
                    print(transaction[0].strftime('%Y-%m-%d %H:%M:%S'), "-", transaction[1], "-", transaction[2])
            else:
                print("No transactions yet.")

    else:
        print("Invalid Input")
