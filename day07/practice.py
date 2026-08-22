"""
给定：
orders = [
    {"customer": "Alice", "product": "MacBook", "category": "Electronics", "price": 1200},
    {"customer": "Bob", "product": "Mouse", "category": "Electronics", "price": 50},
    {"customer": "Alice", "product": "Keyboard", "category": "Electronics", "price": 100},
    {"customer": "Tom", "product": "Python Book", "category": "Books", "price": 40},
    {"customer": "Bob", "product": "SQL Book", "category": "Books", "price": 35},
    {"customer": "Jack", "product": "Monitor", "category": "Electronics", "price": 300},
    {"customer": "Alice", "product": "Python Book", "category": "Books", "price": 40},
    {"customer": "Tom", "product": "Mouse", "category": "Electronics", "price": 50}
]

你的任务

程序自己分析数据，最终输出：
===== Order Analysis =====
Orders: 8
Total sales: 1815
Average order: 226.875
Unique customers: 4
Electronics orders: 5
Books orders: 3
High value orders: 2
Customers: {'Alice', 'Bob', 'Tom', 'Jack'}
Alice total: 1340
Top customer: Alice
==========================

Orders：订单总数。
Total sales：所有 price 加起来。
Average order：
Total sales / Orders
Unique customers：不同顾客数量，同一个人买多次只算一个人。
Electronics orders / Books orders：分别统计两个 category 的订单数量。
High value orders：price >= 300
Customers：保存所有不同顾客的 Set。
Alice total：只统计 Alice 的所有消费
Top customer：找出总消费最高的顾客
"""
orders = [
    {"customer": "Alice", "product": "MacBook", "category": "Electronics", "price": 1200},
    {"customer": "Bob", "product": "Mouse", "category": "Electronics", "price": 50},
    {"customer": "Alice", "product": "Keyboard", "category": "Electronics", "price": 100},
    {"customer": "Tom", "product": "Python Book", "category": "Books", "price": 40},
    {"customer": "Bob", "product": "SQL Book", "category": "Books", "price": 35},
    {"customer": "Jack", "product": "Monitor", "category": "Electronics", "price": 300},
    {"customer": "Alice", "product": "Python Book", "category": "Books", "price": 40},
    {"customer": "Tom", "product": "Mouse", "category": "Electronics", "price": 50}
]
order_count = len(orders)
electronics_order = 0
book_order = 0
high_value_order = 0
customers = set()
name_price = {}

for order in orders:
    name = order["customer"]
    category = order["category"]
    price = order["price"]
    customers.add(name)
    if name in name_price:
        name_price[name] = name_price[name] + price
    else:
        name_price[name] = price

    if category == "Electronics":
        electronics_order += 1
    elif category == "Books":
        book_order += 1

    if price >= 300:
        high_value_order += 1

alice_total = name_price["Alice"]
total_sales = sum(name_price.values())
top_customer = ""
top_value = 0
for customer in name_price:
    if name_price[customer] >= top_value:
        top_value = name_price[customer]
        top_customer = customer

average_order = total_sales / order_count
unique = len(customers)

print("===== Order Analysis =====")
print(f"Orders: {order_count}")
print(f"Total sales: {total_sales}")
print(f"Average order: {average_order}")
print(f"Unique customers: {unique}")
print(f"Electronics orders: {electronics_order}")
print(f"Books orders: {book_order}")
print(f"High value orders: {high_value_order}")
print(f"Customers: {customers}")
print(f"Alice total: {alice_total}")
print(f"Top customer: {top_customer}")
print("==========================")

