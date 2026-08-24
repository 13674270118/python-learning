"""
Class Attribute：
category = "Vehicle"

Instance Attributes：
brand
price
"""
class Car:
    # Class Attribute
    category = "Vehicle"

    def __init__(self, brand, price):
        # Instance Attributes
        self.brand = brand
        self.price = price

car1 = Car("BMW", 50000)
car2 = Car("Tesla", 60000)

print(Car.category)

print(car1.brand)
print(car1.price)
print(car1.category)

print(car2.brand)
print(car2.price)
print(car2.category)


