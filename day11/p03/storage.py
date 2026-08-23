import config
import json

def load_products():
    with open(config.PRODUCTS_FILE, "r") as file:
        products = json.load(file)
    return products

def show_config():
    print(config.PRODUCTS_FILE)
    print(config.SALES_FILE)
    print(config.DEFAULT_PRODUCTS["apple"]["price"])

show_config()

