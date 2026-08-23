class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

apple = Product("apple", 5, 10)
mac = Product("mac", 1000, 3)

print(apple.name)
print(apple.price)
print(apple.stock)



