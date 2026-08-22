"""
使用刚创建的：
data/products.txt

写程序把：
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
写入文件
apple - Price: 5, Stock: 10
mac - Price: 1000, Stock: 3
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
file = open("data/products.txt", "w")
for product in products:
    name = product
    price = products[name]["price"]
    stock = products[name]["stock"]
    file.write(f"{name} - Price: {price}, Stock: {stock}\n")

file.close()







