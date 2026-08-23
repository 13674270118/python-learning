"""
quantity <= 0
→ raise ValueError("Quantity must be greater than 0")
合法
→ return quantity
"""

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    else:
        return quantity

