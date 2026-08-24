class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > self._balance:
            return False
        else:
            self._balance -= amount
            return True


account = BankAccount("James", 1000)

print(account.balance)

account.deposit(500)
print(account.balance)

account.withdraw(200)
print(account.balance)

