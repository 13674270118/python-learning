"""
def validate_price(price):
    ...

def validate_quantity(quantity):
    ...

def calculate_total(price, quantity):
    ...

要求：
validate_price(price)

price < 0
→ raise ValueError("Price cannot be negative")
否则
→ return price
以及：

validate_quantity(quantity)

quantity <= 0
→ raise ValueError("Quantity must be greater than 0")
否则
→ return quantity
"""
def validate_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative")
    else:
        return price

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    else:
        return quantity

def calculate_total(price, quantity):
    return validate_price(price) * validate_quantity(quantity)


print(calculate_total(10, 3))
print(calculate_total(0, 3))
print(calculate_total(10, 0))







