"""
用户输入：
    name
    age
程序输出一段类似：
    Hello Yue
    You are 24 years old.
    Next year you will be 25.
input()、int()、变量、print()，并且计算下一年的年龄。
"""
name = input("enter your name: ")
age = input("enter your age: ")

print("Hello " + name)
print("You are " + age + " years old.")
print("Next year you will be " + str(int(age) + 1) + ".")

age = int(age)
print(f"Hello {name}")
print(f"You are {age} years old.")
print(f"Next year you will be {age + 1}.")



