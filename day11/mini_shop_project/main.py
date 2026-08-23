import storage
import products
import validation

"""
while True
    ↓
input("Enter quantity: ")
    ↓
int(...)
    ↓
validation.validate_quantity(...)
    ↓
ValueError → 打印错误 → 重新输入
    ↓
合法 → return quantity
"""
def ask_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            validation.validate_quantity(quantity)
        except ValueError as e:
            print(e)
        else:
            return quantity

def ask_product():
    product = input("Product name: ")
    return product


def main():
    p = storage.load_products()
    products.show_products(p)
    product = ask_product()
    quantity = ask_quantity()
    total = products.sell_product(p, product, quantity)
    if total is None:
        print("failed")
    else:
        storage.save_products(p)
        print(total)

if __name__ == "__main__":
    main()






