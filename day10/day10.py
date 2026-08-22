# Exception
"""
int("hello") -> ValueError
"10" + 5 -> TypeError
{"apple": 5}["mac"] -> KeyError
[10, 20][5] -> IndexError
10 / 0 -> ZeroDivisionError
open("not_exist.txt", "r") -> FileNotFoundError
"""

# 捕获多个异常
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(a / b)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

# try / except / else
try:
    number = int(input("Enter number: ")) # 100
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful") # run

# finally
try:
    x = int("10")
except ValueError:
    print("Invalid")
else:
    print("Success")
finally:
    print("Finished")

# 获取异常信息
try:
    number = int("hello")
except ValueError as e:
    print(e)

# raise 主动抛出异常
quantity = -10
if quantity <= 0:
    raise ValueError("Quantity must be greater than 0")

# while + try/except —— 让用户重新输入
while True:
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Invalid number")
    else:
        break

# break 和 return 的区别
def get_number():
    while True:
        try:
            number = int(input("Enter number: "))
        except ValueError:
            print("Invalid number")
        else:
            return number

# 损坏的 JSON 与 JSONDecodeError
import json
try:
    with open("data/products.json", "r") as file:
        products = json.load(file)

except FileNotFoundError:
    print("File not found")

except json.JSONDecodeError:
    print("Invalid JSON")







