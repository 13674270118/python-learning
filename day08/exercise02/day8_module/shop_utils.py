"""
calculate_total(100, 3)
→ 300

apply_discount(300, 0.2)
→ 240.0

check_stock(10, 3)
→ True

check_stock(2, 3)
→ False
"""

def calculate_total(price, quantity):
    return price * quantity

def apply_discount(total, discount):
    return total * (1 - discount)

def check_stock(stock, quantity):
    return stock >= quantity


