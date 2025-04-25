class Bank:
    def __init__(self):
        # Dictionary to store account details: {account_number: [name, balance]}
        self.accounts = {}
    

    def create_account(self, name, account_number, initial_balance=0):
        if account_number in self.accounts:
            return "Account already exists!"
        self.accounts[account_number] = [name, initial_balance]
        return f"Account created successfully for {name} with Account Number: {account_number}"
    def dispaly_account(self):
        return self.accounts

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist!"
        self.accounts[account_number][1] += amount
        return f"Deposit successful! New Balance: {self.accounts[account_number][1]}"

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist!"
        if self.accounts[account_number][1] < amount:
            return "Insufficient balance!"
        self.accounts[account_number][1] -= amount
        return f"Withdrawal successful! New Balance: {self.accounts[account_number][1]}"

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            return "Account does not exist!"
        return f"Current Balance for Account {account_number}: {self.accounts[account_number][1]}"

# Example Usage
bank = Bank()

# Create accounts
print(bank.create_account("Pulkit", 101, 5000))
print(bank.create_account("Amit", 102, 3000))
print(bank.dispaly_account())
# Deposit money
print(bank.deposit(101, 2000))

# Withdraw money
print(bank.withdraw(102, 1000))

# Check balance
print(bank.check_balance(101))

# Attempting to withdraw more than the balance
print(bank.withdraw(102, 5000))