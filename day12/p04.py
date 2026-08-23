"""
account1 = BankAccount("James", 1000)
account1.deposit(200)
account1.deposit(300)

print(account1.get_balance())
1500
"""

"""
如果 amount > balance
→ 不修改 balance
→ return False
否则
→ balance -= amount
→ return True
"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

account1 = BankAccount("James", 1000)

print(account1.withdraw(300))
print(account1.balance)

print(account1.withdraw(800))
print(account1.balance)



