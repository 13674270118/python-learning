"""
用户输入一个年龄
如果年龄 大于等于 18，输出：
    Adult
"""
age = int(input("enter your age: "))
if age >= 18:
    print("Adult")

"""
用户输入一个整数 score。
如果 score >= 60，输出 "Pass"
否则输出 "Fail"
要求使用 input()、int()、if、else。
"""
score = int(input("enter an integer: "))
if score >= 60:
    print("Pass")
else:
    print("Fail")

"""
用户输入 score：
90–100 → A
80–89  → B
70–79  → C
60–69  → D
< 60   → F
"""
score = int(input("enter an integer: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
