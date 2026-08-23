"""
# ① 导入 validation
def calculate_total(price, quantity):
    # ② 调用 validation.py 的 validate_quantity()

    # ③ 返回 price * quantity
"""
import validation

def calculate_total(price, quantity):
    validation_quantity = validation.validate_quantity(quantity)
    return price * validation_quantity

