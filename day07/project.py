"""
Mini Shop Management System
程序启动：
===== Mini Shop Management System =====
1. Add product
2. View products
3. Search product
4. Sell product
5. Statistics
6. Exit
Choose:

核心数据结构：
products = []

每个商品保存成 Dictionary：
{
    "name": "MacBook",
    "category": "Electronics",
    "price": 1200,
    "stock": 5,
    "sold": 0
}

功能 1：Add product
用户输入：
Name: MacBook
Category: Electronics
Price: 1200
Stock: 5
加入 products。
如果商品已经存在，暂时直接输出：
Product already exists

功能 2：View products
如果没有商品：
No products
否则输出类似：
===== Products =====
MacBook - Electronics - $1200 - Stock: 5 - Sold: 0
Mouse - Electronics - $50 - Stock: 10 - Sold: 0

功能 3：Search product
用户：
Enter product name: MacBook

找到后输出：
Name: MacBook
Category: Electronics
Price: 1200
Stock: 5
Sold: 0

找不到：
Product not found

功能 4：Sell product
用户输入：
Product: MacBook
Quantity: 2

如果存在并且库存够：
Sale successful

如果商品不存在：
Product not found

如果库存不足：
Not enough stock

功能 5：Statistics
如果没有商品：
No products

否则统计：
===== Statistics =====
Products: 3
Total stock: 18
Total units sold: 7
Revenue: 2750
Top selling product: Mouse
Categories: {'Electronics', 'Books'}

Products：商品种类数量。
Total stock：所有商品剩余库存总和。
Total units sold：所有商品 sold 总和。
Revenue：每个商品：price × sold 全部加起来
Top selling product：找 sold 最大的商品

Categories：用 Set 保存所有不同 category

功能 6：Exit
输出：
Goodbye!
"""

products = []
added_products = set()
while True:
    print("===== Mini Shop Management System =====")
    print("1. Add product")
    print("2. View products")
    print("3. Search product")
    print("4. Sell product")
    print("5. Statistics")
    print("6. Exit")
    choice = int(input("Choose: "))

    product = {}

    if choice == 6:
        print("Goodbye!")
        break
    elif choice == 1:
        name = input("Name: ")
        category = input("Category: ")
        price = int(input("Price: "))
        stock = int(input("Stock: "))

        if name in added_products:
            print("Product already exists")
        else:
            product["name"] = name
            product["category"] = category
            product["price"] = price
            product["stock"] = stock
            product["sold"] = 0

            products.append(product)
            added_products.add(name)


    elif choice == 2:
        if len(products) == 0:
            print("No products")
        else:
            print("===== Products =====")
            for p in products:
                name = p["name"]
                category = p["category"]
                price = p["price"]
                stock = p["stock"]
                sold = p["sold"]
                print(f"{name} - {category} - ${price} - Stock: {stock} - Sold: {sold}")

    elif choice == 3:
        search_name = input("Enter product name: ")
        has_product = False
        for p in products:
            name = p["name"]
            if search_name == name:
                has_product = True
                category = p["category"]
                price = p["price"]
                stock = p["stock"]
                sold = p["sold"]
                print(f"Name: {name}")
                print(f"Category: {category}")
                print(f"Price: {price}")
                print(f"Stock: {stock}")
                print(f"Sold: {sold}")

        if not has_product:
            print("Product not found")

    elif choice == 4:
        search_name = input("Product: ")
        quantity = int(input("Quantity: "))
        has_product = False
        for p in products:
            if p["name"] == search_name:
                has_product = True
                stock = p["stock"]
                sold = p["sold"]
                if stock >= quantity:
                    p["stock"] = p["stock"] - quantity
                    p["sold"] = p["sold"] + quantity
                    print("Sale successful")
                else:
                    print("Not enough stock")
        if not has_product:
            print("Product not found")

    elif choice == 5:
        if len(products) == 0:
            print("No products")
        else:
            products_count = len(products)
            total_stock = 0
            total_sold = 0
            revenue = 0
            categories = set()
            product_sold = {}
            for p in products:
                name = p["name"]
                category = p["category"]
                price = p["price"]
                stock = p["stock"]
                sold = p["sold"]

                revenue += price * sold
                total_stock += stock
                total_sold += sold
                categories.add(category)

                if name in product_sold:
                    product_sold[name] += sold
                else:
                    product_sold[name] = sold

            top_sold = 0
            top_product = ""
            for p, s in product_sold.items():
                if s >= top_sold:
                    top_product = p
                    top_sold = s

            print("===== Statistics =====")
            print(f"Products: {products_count}")
            print(f"Total stock: {total_stock}")
            print(f"Total units sold: {total_sold}")
            print(f"Revenue: {revenue}")
            print(f"Top selling product: {top_product}")
            print(f"Categories: {categories}")









