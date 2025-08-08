import pathlib as Path

class Account():
    def __init__(self,name,account_number,balance = 0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.all_transactions = []
    def deposit(self,amount):
        self.balance += amount
        self.all_transactions.append(f"Deposited: ${amount}")
        print(f"Deposited ${amount}. New balance is ${self.balance}")
    def withdraw(self,amount,balance):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            self.all_transactions.append(f'Withdrew: ${amount}')
            print(f"Withdrew ${amount}. New balance is ${self.balance}")
    def view_balance(self):
        print(f"Current balance: ${self.balance}")
    def view_transactions(self):
        print("Transaction History:")
        for transaction in self.all_transactions:
            print(transaction)

user = input("Enter your name:")
account_number = input("Enter your account number:")
account = Account(user, account_number)

while True:
    action = input("What would you like to do? (deposit,withdraw,view balance,view transactions,exit):").strip().lower()
    if action == 'deposit':
        amount = float(input("Enter amount to deposit:"))
        account.deposit(amount)
    elif action == 'withdraw':
        amount = float(input("Enter amount to withdraw:"))
        account.withdraw(amount, account.balance)
    elif action == 'view balance':
        account.view_balance()
        continue
    elif action == 'view transactions':
        account.view_transactions()
        continue
    elif action == 'exit':
        print("Exiting the account management system. Goodbye!")
        break

    
file_path = Path('account_data.txt')
if not file_path.exists():
    with open(file_path,'w') as file:
        file.write('')
