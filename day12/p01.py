"""
完成：
# ① 创建一个 Student Class
# 目前里面什么都不用写

# ② 创建两个不同对象
student1 = ???
student2 = ???

# ③ 打印两个对象的 type

# ④ 使用 isinstance() 判断：
# student1 是否是 Student

要求最终类似：
<class '__main__.Student'>
<class '__main__.Student'>
True
"""
class Student:
    pass

student1 = Student()
student2 = Student()

print(type(student1))
print(type(student2))

print(isinstance(student1, Student))





