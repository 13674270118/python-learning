class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # value < 0
        # → raise ValueError("Price cannot be negative")
        if value < 0:
            raise ValueError("Price cannot be negative")
        # 否则修改 _price
        else:
            self._price = value


apple = Product("apple", 5)

print(apple.price)

apple.price = 6
print(apple.price)

apple.price = -10


