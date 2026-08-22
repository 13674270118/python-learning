"""
def ask_quantity():
    ...

函数内部自己调用：
input("Enter quantity: ")

要求：
如果用户输入：
hello
打印错误，然后重新询问。

如果输入：
-2

主动：
raise ValueError("Quantity must be greater than 0")
然后打印错误，继续询问。

如果输入：
0
同样继续询问。

只有输入：
5
这样的正整数时：
return 5

最终：
quantity = ask_quantity()
print("Quantity:", quantity)

假设用户依次输入：
hello
-2
0
5

程序应该类似：
Enter quantity: hello
Invalid quantity: ...
Enter quantity: -2
Invalid quantity: Quantity must be greater than 0
Enter quantity: 0
Invalid quantity: Quantity must be greater than 0
Enter quantity: 5
Quantity: 5
"""
def ask_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0")
        except ValueError as e:
            print(f"Invalid quantity: {e}")
        else:
            return quantity

ask_quantity()





