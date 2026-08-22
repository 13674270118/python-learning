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

第一次运行
JSON stock 10
     ↓
卖 3 个
     ↓
stock 7
     ↓
保存 JSON
程序关闭
────────────
第二次运行
     ↓
读取 JSON
     ↓
stock 7 ✅
"""
import json
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

def load_products():
    try:
        with open("data/products.json", "r") as file:
            loaded_products = json.load(file)
        return loaded_products
    except FileNotFoundError:
        return products


def save_products(products):
    with open("data/products.json", "w") as file:
        json.dump(products, file, indent=4)

def show_products(products):
    if len(products) == 0:
        print("No product")
    for k, v in products.items():
        print(f"{k} - Price: {v['price']}, Stock: {v['stock']}")

def sell_product(products, name, quantity):
    if name not in products:
        return None
    elif products[name]["stock"] < quantity:
        return None
    else:
        products[name]["stock"] -= quantity
        return products[name]["price"] * quantity

def save_sale(name, quantity, total):
    with open("data/sales.txt", "a") as file:
        file.write(f"{name},{quantity},{total}\n")


# save_products(products)

products = load_products()

show_products(products)

total = sell_product(products, "apple", 3)

if total is not None:
    save_products(products)
    save_sale("apple", 3, total)
    print(f"Sale successful. Total: {total}")
else:
    print("Sale failed.")

print()
show_products(products)



