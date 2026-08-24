# 定义 Class Attribute
class Product:
    shop_name = "Mini Shop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Encapsulation 封装
# 希望对象的数据不要被外部代码随意修改

# _attribute——内部属性约定
# balance 是对象内部维护的数据，最好不要从外面随便修改
# _balance 一种程序员之间的命名约定
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            return False
        else:
            self._balance -= amount
            return True

# @property
class BankAccount1:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return round(self._balance, 2)

account = BankAccount1("James", 1000)
print(account.balance)

# @property.setter
class BankAccount2:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value




