# Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdrawal(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! New balance: ${self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            print("Insufficient funds! Withdrawal denied.")

    def __str__(self):
        return f"Bank Account Owner: {self.owner}\nBalance: {self.balance}"


p1 = bank("Balaussa", 200)
print(p1)
p1.deposit(30)
p1.withdrawal(400)
p1.withdrawal(50)
p1.deposit(15)
print(p1)


        

    