class BankAccount:
    def __init__(self, owner, balance):
        # owner 正常公开
        self.owner = owner
        # balance 保存为 _balance
        self._balance = balance

    def deposit(self, amount):
        # _balance 增加
        self._balance += amount

    def withdraw(self, amount):
        # 如果 amount > _balance
        # return False
        if amount > self._balance:
            return False

        # 否则减少 _balance
        # return True
        self._balance -= amount
        return True

    def get_balance(self):
        # return _balance
        return self._balance


account = BankAccount("James", 1000)

account.deposit(500)
print(account.get_balance())

print(account.withdraw(200))
print(account.get_balance())

print(account.withdraw(2000))
print(account.get_balance())