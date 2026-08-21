# print() 和变量
print("hello, python!")

name = "james"
age = 23

print(name)
print(age)

name = "yue"
age = 24
major = "student"
print(name)
print(age)
print(major)

# Python 的基本数据类型
name = "yue" # str
age = 24 # int
height = 1.80 # float
is_student = True # bool

print(type(name))

city = "fujian"
year = 2001
temperature = 10.31
is_raining = True

print(type(city))
print(type(year))
print(type(temperature))
print(type(is_raining))

# 变量之间的计算
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(17//5) # 3
print(17%5) # 2

# 字符串 str 的基本操作
name = "yue"
first_name = "yue"
last_name = "lin"
full_name = first_name +" "+ last_name
print(full_name)

# input() 获取用户输入
name = input("enter your name: ")
print(name)

# E: 让用户输入自己的年龄，然后输出 10 年后的年龄
age = int(input("your age: "))
age_10 = age + 10
print(age_10)

# 比较运算符
age = 24
print(age > 18)
print(age < 18)
print(age == 18)

# if 条件判断
age = 20
if age >= 18:
    print("Adult")

# 逻辑运算
# 年龄至少 18 岁，并且有驾照，才能开车
age = 20
has_license = True
if age >= 18 and has_license:
    print("can drive")

is_student = True
is_senior = False
if is_student or is_senior:
    print("Discount")

is_raining = False
if not is_raining:
    print("Go outside")



