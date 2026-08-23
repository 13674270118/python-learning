import validation

"""
apple - Price: 5, Stock: 10
mac - Price: 1000, Stock: 3
"""
def show_products(products):
    for k, v in products.items():
        print(f"{k} - Price: {v['price']}, Stock: {v['stock']}")

"""
商品不存在
→ return None
validation.validate_quantity(quantity)
库存不足
→ return None
库存足够
→ 减少 stock
→ return price * quantity
"""
def sell_product(products, name, quantity):
    if name not in products:
        return None
    validation.validate_quantity(quantity)
    stock = products[name]['stock']
    if stock < quantity:
        return None
    else:
        products[name]['stock'] -= quantity
        return products[name]['price'] * quantity

