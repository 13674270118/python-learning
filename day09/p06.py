"""
完成：
import json
def save_products(products):
    # TODO

def load_products():
    # TODO

然后测试：
products = load_products()
print("Before:", products["apple"]["stock"])
products["apple"]["stock"] -= 2
save_products(products)
products = load_products()
print("After:", products["apple"]["stock"])
"""
import json

def save_products(products):
    with open("data/test.json", "w") as file:
        json.dump(products, file, indent=4)

def load_products():
    with open("data/test.json", "r") as file:
        products = json.load(file)

    return products

# products = {
#     "apple": {"stock": 10}
# }

products = load_products()
print("Before:", products["apple"]["stock"])
products["apple"]["stock"] -= 2
save_products(products)
products = load_products()
print("After:", products["apple"]["stock"])
