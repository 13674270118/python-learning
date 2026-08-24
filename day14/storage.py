import json
from product import Product

def save_products(products):
    data = {}
    for name, product in products.items():
        data[name] = {
            "price": product.price,
            "stock": product.stock
        }

    with open("data/products.json", "w") as file:
        json.dump(data, file, indent=4)

def load_products():
    products = {}
    try:
        with open("data/products.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON")
        return {}
    else:
        for name, detail in data.items():
            product = Product(name, detail["price"], detail["stock"])
            products[name] = product
        return products

