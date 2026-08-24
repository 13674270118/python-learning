"""
self.name
self._price
self.stock

@property
def price(self):
    ...
"""

class Product:
    category = "General"

    def __init__(self, name, price, stock):
        self.name = name
        self._price = price
        self.stock = stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        """
        value < 0
        → raise ValueError("Price cannot be negative")

        否则
        → 修改 self._price
        """
        if value < 0:
            raise ValueError("Price cannot be negative")

        self._price = value

    def sell(self, quantity):
        """
        quantity <= 0
        → raise ValueError("Quantity must be greater than 0")

        quantity > stock
        → return None

        成功
        → stock -= quantity
        → return price × quantity
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        elif quantity > self.stock:
            return None
        else:
            self.stock -= quantity
            return self.price * quantity

    def show_info(self):
        print(f"{self.name} - Price: {self.price}, Stock: {self.stock}")

class DigitalProduct(Product):
    def __init__(self, name, price, stock, download_link):
        super().__init__(name, price, stock)
        self.download_link = download_link

    def show_info(self):
        print(f"{self.name} - Price: {self.price}, Stock: {self.stock}, Download: {self.download_link}")


products = {
    "apple": Product("apple", 5, 10),
    "course": DigitalProduct(
        "Python Course",
        100,
        5,
        "python.com/download"
    )
}

products["apple"].show_info()
products["course"].show_info()

print(products["apple"].sell(3))
print(products["apple"].stock)

print(products["course"].sell(2))
print(products["course"].stock)

products["apple"].price = 6
print(products["apple"].price)

print(isinstance(products["course"], Product))
print(isinstance(products["course"], DigitalProduct))

