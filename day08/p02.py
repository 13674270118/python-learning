"""
完成下面这道题：
def add_product(name, price, stock=0, category="General"):
    # 你的代码
# 1. 只传 name 和 price
add_product(...)
# 2. 修改 stock，但使用默认 category
add_product(...)
# 3. 同时修改 stock 和 category
add_product(...)

要求每次输出：
Product: xxx
Price: xxx
Stock: xxx
Category: xxx
"""
def add_product(name, price, stock=0, category="General"):
    print(f"Product: {name}")
    print(f"Price: {price}")
    print(f"Stock: {stock}")
    print(f"Category: {category}")

add_product("mac", 10)
add_product("mac", 10, 5)
add_product("mac", 10, 5, "elec")




