# 函数参数
# 位置参数 Positional Arguments
def introduce(name, age):
    print(f"My name is {name}, I am {age} years old")

introduce("James", 23)

# 关键字参数 Keyword Arguments
introduce(name = "James", age = 23)

# 默认参数 Default Arguments
def create_user(username, age, city="Hong Kong"):
    print(f"User {username} is {age} years old and lives in {city}")

# *args
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3, 4))

# 变量作用域 Scope
# Local Variable 局部变量
def test():
    x = 10
    print(x)

test()

# Lambda 表达式
# 一个很短、没有名字的函数

# def square(x):
#     return x ** 2

square = lambda x: x**2
print(square(5))

# 函数作为参数
def add(a, b):
    return a + b

def calculate(a, b, operation):
    return operation(a, b)

result = calculate(10, 5, add)
print(result)

# random 模块
import random
number = random.randint(1, 10) # 随机生成 1～10，包括 1 和 10 的整数



