from product import Product
from manager import ProductManager
import storage

"""
===== Mini Shop Management System =====
1. Add product
2. View products
3. Search product
4. Sell product
5. Exit
"""
def show_menu():
    print("===== Mini Shop Management System =====")
    print("1. Add product")
    print("2. View products")
    print("3. Search product")
    print("4. Sell product")
    print("5. Exit")

def main():
    manager = ProductManager()
    manager.products = storage.load_products()

    """
    显示菜单
    ↓
    输入 choice
    ↓
    根据 choice 执行功能
    """
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "2":
            manager.show_products()
        elif choice == "5":
            print("Goodbye")
            break
        elif choice == "1":
            while True:
                try:
                    name = input("Product name: ")
                    price = float(input("Price: "))
                    stock = int(input("Stock: "))
                except ValueError as e:
                    print(f"Invalid input: {e}")
                else:
                    product = Product(name, price, stock)
                    flag = manager.add_product(product)
                    if flag:
                        storage.save_products(manager.products)
                        print("Product added")
                    else:
                        print("Product already exists")

                    break

        elif choice == "3":
            name = input("Product name: ")
            product = manager.search_product(name)
            if product is None:
                print("Product not found")
            else:
                product.show_info()

        elif choice == "4":
            while True:
                try:
                    name = input("Product name: ")
                    quantity = int(input("Quantity: "))
                except ValueError as e:
                    print(f"Invalid input: {e}")
                else:
                    try:
                        total = manager.sell_product(name, quantity)
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                    else:
                        if total is None:
                            print("Sale failed")
                            break
                        else:
                            storage.save_products(manager.products)
                            print(f"Sale successful. Total: {total}")
                            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
