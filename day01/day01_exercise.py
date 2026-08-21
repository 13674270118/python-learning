"""
奇数还是偶数
用户输入一个整数
程序判断它是偶数还是奇数
要求使用 input()、int()、%、if / else
"""
number = int(input("enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
用户输入：
    age
    score
age < 18
→ 输出 "Too young"
age >= 18 并且 score >= 80
→ 输出 "Excellent"
age >= 18 并且 score >= 60
→ 输出 "Pass"
其他情况
→ 输出 "Fail"
"""
age = int(input("enter your age: "))
score = int(input("enter your score: "))
if age < 18:
    print("Too young")
else:
    if score >= 80:
        print("Excellent")
    elif score >= 60:
        print("Pass")
    else:
        print("Fail")

"""
找最大值
用户输入三个整数
程序输出三个数字中的最大值
"""
a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print(largest)



