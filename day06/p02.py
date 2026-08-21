"""
给定：
product = {
    "name": "MacBook",
    "price": 1200,
    "stock": 15
}

要求使用 一个 for 循环 + items() 输出：
name: MacBook
price: 1200
stock: 15
"""
product = {
    "name": "MacBook",
    "price": 1200,
    "stock": 15
}
for key, value in product.items():
    print(f"{key}: {value}")


