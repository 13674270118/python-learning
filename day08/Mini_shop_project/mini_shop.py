"""
① show_products
调用：
show_products(products)

输出类似：
apple - Price: 5, Stock: 10
mac - Price: 1000, Stock: 3

② search_product
product = search_product(products, "apple")
print(product)
返回：
{"price": 5, "stock": 10}
如果不存在，例如：
search_product(products, "iphone")
返回：
None

③ calculate_total
calculate_total(5, 3)
返回：
15

④ sell_product
sell_product(products, "apple", 3)
需要：
检查商品是否存在
检查库存是否足够
库存足够 → 减少库存
返回本次销售总价
商品不存在或库存不足 → 返回 None

例如原来：
apple stock = 10
执行：
total = sell_product(products, "apple", 3)
之后：
total = 15
apple stock = 7
"""
products = {
    "apple": {
        "price": 5,
        "stock": 10
    },
    "mac": {
        "price": 1000,
        "stock": 3
    }
}


def show_products(products):
    for product, detail in products.items():
        price = detail["price"]
        stock = detail["stock"]
        print(f"{product} - Price: {price}, Stock: {stock}")


def search_product(products, name):
    if name in products.keys():
        return products[name]
    else:
        return None


def calculate_total(price, quantity):
    return price * quantity


def sell_product(products, name, quantity):
    if name in products.keys():
        stock = products[name]["stock"]
        if stock >= quantity:
            products[name]["stock"] = products[name]["stock"] - quantity
            return products[name]["price"] * quantity
        else:
            return None
    else:
        return None


show_products(products)

print(search_product(products, "apple"))
print(search_product(products, "iphone"))

total = sell_product(products, "apple", 3)

print("Total:", total)
print("Remaining stock:", products["apple"]["stock"])