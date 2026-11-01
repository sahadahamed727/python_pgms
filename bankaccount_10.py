class BankAccount:
    def __init__(self, account_number, holder_name, account_type, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def display(self):
        print("-" * 30)
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Account Type   : {self.account_type}")
        print(f"Balance        : ${self.balance:.2f}")
        print("-" * 30)


# Example usage
if __name__ == "__main__":
    account = BankAccount("1001234567", "Alice Johnson", "Savings", 500.00)
    account.display()
    account.deposit(250)
    account.withdraw(100)
    account.withdraw(1000)  # Triggers insufficient funds
    account.display()