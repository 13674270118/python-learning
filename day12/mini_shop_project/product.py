"""
quantity <= 0
→ raise ValueError("Quantity must be greater than 0")

quantity > stock
→ return None

否则
→ stock -= quantity
→ return 本次销售总价
"""
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):
        print(f"{self.name} - Price: {self.price}, Stock: {self.stock}")

    def calculate_total(self, quantity):
        return self.price * quantity

    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        elif quantity > self.stock:
            return None
        else:
            self.stock -= quantity
            return self.price * quantity

products = {
    "apple": Product("apple", 5, 10),
    "mac": Product("mac", 1000, 3)
}

def show_products(products):
    for k, v in products.items():
        v.show_info()

"""
name 不存在
→ return None
存在
→ 找到 Product Object
→ 调用它自己的 sell(quantity)
→ return sell() 的结果
"""
def sell_product(products, name, quantity):
    if name not in products:
        return None
    else:
        product = products[name]
        return product.sell(quantity)




