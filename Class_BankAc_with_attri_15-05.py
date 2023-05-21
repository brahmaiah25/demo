# #3.Create a class BankAccount with attributes balance and account_number.
# # Add methods deposit(amount) and withdraw(amount) that add or subtract the amount from the balance, respectively.
# # Create an instance of the class with balance=1000 and account_number="12345". 
# # Deposit 500 into the account, withdraw 200, and print the remaining balance.

class BankAccount:
    def __init__(self,balance,account_number):
        self.balance = balance
        self.account_number = account_number

    def deposit(self,amount):
        self.amount=amount
        self.balance += amount

    def withdraw(self,amount):
        self.amount=amount
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(" Insufficient Funds ")
            
    def remaining_balance(self):
        return self.balance 
    

my_account=BankAccount(balance=1000,account_number="12345")


my_account.deposit(amount=500)
my_account.withdraw(amount=200)

print("Remaining Balance : ",my_account.remaining_balance())