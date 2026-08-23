"""
class Student:
要求初始化时接收：
name
age
major

并保存成：
self.name
self.age
self.major

然后创建：
student1 = Student("James", 23, "Mathematics")
student2 = Student("Tom", 24, "Computer Science")

最后打印：
print(student1.name)
print(student1.age)
print(student1.major)

print(student2.name)
print(student2.age)
print(student2.major)
"""
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

student1 = Student("James", 23, "Mathematics")
student2 = Student("Tom", 24, "Computer Science")

print(student1.name)
print(student1.age)
print(student1.major)

print(student2.name)
print(student2.age)
print(student2.major)


