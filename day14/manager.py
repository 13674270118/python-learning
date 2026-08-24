from product import Product

class ProductManager:
    def __init__(self):
        self.products = {}

    """
    接收一个 Product Object

    用 product.name 当 key
    ↓
    加入 self.products
    """

    """
    如果 product.name 已经存在
    → return False
    → 不覆盖原商品
    
    如果不存在
    → 加入 self.products
    → return True
    """
    def add_product(self, product):
        if product.name in self.products:
            return False
        else:
            self.products[product.name] = product
            return True

    """
    如果没有商品
    → print("No products")
    
    否则
    → 遍历所有 Product Object
    → 调用 product.show_info()
    """
    def show_products(self):
        if len(self.products) == 0:
            print("No products")
        else:
            for product in self.products.values():
                product.show_info()

    """
    name 不存在
    ↓
    return None
    
    name 存在
    ↓
    return 对应的 Product Object
    """
    def search_product(self, name):
        if name not in self.products:
            return None
        else:
            return self.products[name]

    def sell_product(self, name, quantity):
        product = self.search_product(name)
        if product is None:
            return None
        else:
            return product.sell(quantity)



