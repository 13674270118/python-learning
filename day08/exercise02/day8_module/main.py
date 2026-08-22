import shop_utils

print(f"Total: {shop_utils.calculate_total(100, 3)}")
print(f"After discount: {shop_utils.apply_discount(300, 0.2)}")
print(f"Enough stock: {shop_utils.check_stock(3, 2)}")

