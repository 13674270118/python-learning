import json
import config
"""
读取 config.PRODUCTS_FILE
正常
→ return JSON 数据
FileNotFoundError
→ return config.DEFAULT_PRODUCTS
JSONDecodeError
→ print("Invalid JSON")
→ return config.DEFAULT_PRODUCTS
"""
def load_products():
    try:
        with open(config.PRODUCTS_FILE, 'r') as file:
            products = json.load(file)
    except FileNotFoundError:
        return config.DEFAULT_PRODUCTS
    except json.JSONDecodeError:
        print("Invalid JSON")
        return config.DEFAULT_PRODUCTS
    else:
        return products


"""
写入 config.PRODUCTS_FILE
↓
json.dump(..., indent=4)
"""
def save_products(products):
    with open(config.PRODUCTS_FILE, 'w') as file:
        json.dump(products, file, indent=4)


