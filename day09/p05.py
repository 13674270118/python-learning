"""
使用：
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

完成两个步骤。
① 保存
创建：
data/products.json
要求：
json.dump(...)
并使用：
indent=4
② 再读取
从刚才的：
data/products.json
读取到变量：
loaded_products
最后打印：
print(loaded_products)
print(type(loaded_products))
print(loaded_products["mac"]["price"])
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

with open("data/products.json", "w") as file:
    json.dump(products, file, indent=4)

with open("data/products.json", "r") as file:
    loaded_products = json.load(file)

print(loaded_products)
print(type(loaded_products))
print(loaded_products["mac"]["price"])






