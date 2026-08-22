"""
def calculate_total(price, quantity):
    ...

要求：
如果：
price < 0
主动：
raise ValueError("Price cannot be negative")

如果：
quantity <= 0
主动：
raise ValueError("Quantity must be greater than 0")

否则：
return price * quantity
"""
def calculate_total(price, quantity):
    if price < 0:
        raise ValueError("Price cannot be negative")
    elif quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    else:
        return price * quantity
"""
完成：
def get_quantity(value):
    ...

要求：
get_quantity("5")

返回：
5

而：
get_quantity("hello")
需要捕获 int() 产生的 ValueError。

对于：
get_quantity("0")
get_quantity("-3")
需要你自己：
raise ValueError("Quantity must be greater than 0")

最后统一：
except ValueError as e:
    print(f"Invalid quantity: {e}")
    return None
"""
def get_quantity(value):
    try:
        num = int(value)
        if num <= 0:
            raise ValueError("Quantity must be greater than 0")
    except ValueError as e:
        print(f"Invalid quantity: {e}")
        return None
    else:
        return num

print(get_quantity("5"))
print(get_quantity("hello"))
print(get_quantity("0"))
print(get_quantity("-3"))








