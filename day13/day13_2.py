# Inheritance 继承
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
"""
父类已有：
name
price

子类新增：
download_link
"""
class DigitalProduct(Product):
    def __init__(self, name, price, download_link):
        super().__init__(name, price)
        self.download_link = download_link

# Method Override 方法重写
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")