"""
写一个函数：
def divide(a, b):

divide(10, 0)
divide("hello", 2)
"""
def divide(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Invalid type")

divide(10, 2)
divide(10, 0)
divide("hello", 2)


