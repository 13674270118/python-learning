"""
假设 products.txt：
apple - Price: 5, Stock: 10
mac - Price: 1000, Stock: 3

要求逐行读取，并输出：
Product 1: apple - Price: 5, Stock: 10
Product 2: mac - Price: 1000, Stock: 3
"""
with open("data/products.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
        print(f"Product {count}: {line.strip()}")



