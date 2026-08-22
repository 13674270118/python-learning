"""
Data Persistence（数据持久化）

最简单的方法：文件
例如创建：
products.txt
里面保存：
    apple,5,7
    mac,1000,3
程序重新启动后，再读取这个文件。
"""

# open() 与文件路径
# file = open("test.txt", "w") # 打开文件/创建文件
# file.close() # 关闭文件
# "w" 会清空文件原来的内容，然后重新写入
# file = open("data/products.txt", "w")
# file.write("apple") # apple
# file.write("mac") # applemac, write() 不会自动换行

# file.write("\n") # 换行
# file.write("apple\n")
# file.write("mac\n")
# file.close()

# f-string
# name = "apple"
# price = 5
# stock = 10
# file = open("data/products.txt", "w")
# file.write(f"{name} - Price: {price}, Stock: {stock}\n")
# file.close()

# 读取文件 read()
"""
假设 products.txt 已经有：
apple - Price: 5, Stock: 10
mac - Price: 1000, Stock: 3
"""
file = open("data/products.txt", "r")
content = file.read()
print(content)
file.close()

# with open(...) as ...
# 离开 with 代码块以后，Python 自动关闭文件
with open("data/products.txt", "r") as file:
    content = file.read()

print(content)

# 逐行读取文件
with open("data/products.txt", "r") as file:
    for line in file:
        print(line.strip())

# 追加模式 "a"
# "a" 也可以创建文件
with open("data/sales.txt", "a") as file:
    file.write("apple,3,15\n")

with open("data/sales.txt", "a") as file:
    file.write("mac,1,1000\n")

# JSON:一种非常常见的结构化数据保存格式
# json.dump()  → Python → JSON 文件
# json.load()  → JSON 文件 → Python
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

import json

with open("data/products.json", "w") as file:
    json.dump(products, file, indent=4) # indent=4, 让 JSON 更容易阅读

with open("data/products.json", "r") as file:
    products = json.load(file)

print(products)

# 异常处理
try:
    number = int(input("Number: "))
except ValueError:
    print("Please enter a number")
