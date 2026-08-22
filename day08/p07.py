"""
products = [
    ("MacBook", 1200),
    ("Mouse", 30),
    ("iPhone", 999),
    ("Keyboard", 80)
]

使用：
sort()和lambda
把商品按照 price 从高到低 排序
"""
products = [
    ("MacBook", 1200),
    ("Mouse", 30),
    ("iPhone", 999),
    ("Keyboard", 80)
]

products.sort(key=lambda p: p[1], reverse = True)





