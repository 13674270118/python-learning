"""
给定：
import json

DEFAULT_PRODUCTS = {
    "apple": {
        "price": 5,
        "stock": 10
    },
    "mac": {
        "price": 1000,
        "stock": 3
    }
}

完成
def load_products():
    ...

def validate_quantity(quantity):
    ...

def sell_product(products, name, quantity):
    ...

def save_products(products):
    ...

def ask_quantity():
    ...
"""
"""
① load_products()
读取 data/products.json

正常
→ return json.load(file)

文件不存在
→ return DEFAULT_PRODUCTS

JSON 损坏
→ print("Invalid JSON")
→ return DEFAULT_PRODUCTS

② validate_quantity(quantity)
quantity <= 0
→ raise ValueError("Quantity must be greater than 0")
否则
→ return quantity

③ sell_product(products, name, quantity)
商品不存在
→ return None

调用 validate_quantity(quantity)

库存不足
→ return None

成功
→ 减少库存
→ return price * quantity

④ save_products(products)
写入 data/products.json
使用 json.dump(..., indent=4)

⑤ ask_quantity()
while True
input("Enter quantity: ")
→ 转换成 int
→ 调用 validate_quantity()

出现 ValueError
→ print(f"Invalid quantity: {e}")
→ 继续输入

合法
→ return quantity
"""
import json

DEFAULT_PRODUCTS = {
    "apple": {
        "price": 5,
        "stock": 10
    },
    "mac": {
        "price": 1000,
        "stock": 3
    }
}

def load_products():
    try:
        with open("data/products.json", 'r') as file:
            products = json.load(file)
    except FileNotFoundError:
        return DEFAULT_PRODUCTS
    except json.JSONDecodeError:
        print("Invalid JSON")
        return DEFAULT_PRODUCTS
    else:
        return products

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    else:
        return quantity

def sell_product(products, name, quantity):
    if name not in products:
        return None
    validate_quantity(quantity)
    if products[name]["stock"] < quantity:
        return None
    else:
        products[name]["stock"] -= quantity
        return products[name]["price"] * quantity

def save_products(products):
    with open("data/products.json", 'w') as file:
        json.dump(products, file, indent=4)

def ask_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            validate_quantity(quantity)
        except ValueError as e:
            print(f"Invalid quantity: {e}")
        else:
            return quantity

products = load_products()

name = input("Product name: ")
quantity = ask_quantity()

total = sell_product(products, name, quantity)

if total is None:
    print("Sale failed.")
else:
    save_products(products)
    print(f"Sale successful. Total: {total}")
