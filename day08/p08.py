"""
完成三个函数：
def add(a, b):
    ...
def subtract(a, b):
    ...
def calculate(a, b, operation):
    ...

要求下面代码能够工作：
print(calculate(10, 5, add))
print(calculate(10, 5, subtract))

输出：
15
5

再加一个 Lambda
不用定义 multiply()，直接使用 lambda：
print(calculate(10, 5, ???))

输出：
50
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(a, b, operation):
    return operation(a, b)

print(calculate(10, 5, add))
print(calculate(10, 5, subtract))
print(calculate(10, 5, lambda a, b: a * b))






