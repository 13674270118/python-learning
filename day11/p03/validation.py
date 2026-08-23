def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity

