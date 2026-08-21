# Tuple
# 允许重复
scores = (85, 90, 95)
student = ("Alice", 20, 92.5, True)
empty = ()
data = (10,)

# Tuple 常用操作
numbers = (10, 20, 30, 20, 40, 20)
print(len(numbers))
print(numbers.count(20))
print(numbers.index(20))

# Tuple Unpacking
student = ("Yue", 24, 95)
name, age, score = student

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Tom", 58)
]

for name, score in students:
    print(name, score)

# set
numbers = {1, 2, 3, 4}
# 不重复
numbers = {1, 2, 2, 3, 3, 3} # {1, 2, 3}

empty = set()

# Set 添加与删除
numbers.add(4) # 1, 2, 3, 4
numbers.remove(3) # 1, 2 ,4
numbers.discard(3) # 1, 2, 4, 删除不存在的数字不会报错

# Set 交集 / 并集 / 差集
python_students = {"Alice", "Bob", "Tom", "Yue"}
java_students = {"Bob", "Tom", "Jack"}

# Intersection：交集
# 同时学习 Python 和 Java 的学生
print(python_students & java_students)
print(python_students.intersection(java_students))

# Union：并集
# 学习 Python 或者 Java 的所有学生
print(python_students | java_students)
print(python_students.union(java_students))

# Difference：差集
# 学 Python、但是没有学 Java的人
print(python_students - java_students)





