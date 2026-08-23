"""
给定：
class BankAccount:
    def __init__(self, owner, balance):
        # TODO
① 保存两个实例属性
owner
balance
② 创建
account1 = BankAccount("James", 1000)
account2 = BankAccount("Tom", 500)
③ 修改
只修改：
account1.balance
让它增加 200
④ 打印
print(account1.owner, account1.balance)
print(account2.owner, account2.balance)
"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account1 = BankAccount("James", 1000)
account2 = BankAccount("Tom", 500)

account1.balance += 200

print(account1.owner, account1.balance)
print(account2.owner, account2.balance)


