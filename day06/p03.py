"""
给定：
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Tom", "score": 58},
    {"name": "Jack", "score": 76}
]

创建一个空 List：
excellent_students = []
遍历 students，把：
score >= 80
的学生姓名添加进去。
最终：
Excellent: ['Alice', 'Bob']
"""
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Tom", "score": 58},
    {"name": "Jack", "score": 76}
]
excellent = []
for student in students:
    if student["score"] >= 80:
        excellent.append(student["name"])

print(excellent)