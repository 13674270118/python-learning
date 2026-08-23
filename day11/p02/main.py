"""
下面这个 calculator.py 有问题：
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print("Testing calculator")

print(add(10, 5))
print(multiply(10, 5))

现在要求：
直接运行
python calculator.py

仍然输出：
Testing calculator
15
50

但是如果：
import calculator
不能自动打印任何东西。
"""
import calculator

