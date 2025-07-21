# WAP make a class in which the bank and account number will be given and the amount will be deposited and withdrawn.
class Bank:
    space = print("\n \n")
    def __init__(self, account_number, amount):
        self.account_number = account_number
        self.amount = amount
        print(f"Bank Account Number: {self.account_number}")
        print(f"Initial Amount: {self.amount}")

    def deposit(self, deposit_amount):
        self.amount += deposit_amount
        print(f"Deposited Amount: {deposit_amount}")
        print(f"New Balance: {self.amount}")

    def withdraw(self, withdraw_amount):
        self.amount -= withdraw_amount
        print(f"Withdrawn Amount: {withdraw_amount}")
        print(f"New Balance: {self.amount}")

    def space(self):
        print("\n \n")

        
# Create an instance of the Bank class
b1 = Bank("123456789", 1000)
b1.deposit(500) 
b1.withdraw(200)
b1.space()

# Create another instance of the Bank class
b2 = Bank("987654321", 2000)
b2.deposit(1000)
b2.withdraw(300)

    