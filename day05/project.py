"""
Course Enrollment Analyzer(课程选课分析器)
给定以下数据：

enrollments = [
    ("Alice", "Python"),
    ("Bob", "Java"),
    ("Tom", "Python"),
    ("Alice", "Java"),
    ("Jack", "Java"),
    ("Bob", "Python"),
    ("Yue", "Python"),
    ("Tom", "Java"),
    ("Alice", "Python"),
    ("Jack", "Java")
]

最终要求

程序输出类似：
===== Course Enrollment Analyzer =====
Python students: 4
Java students: 4
Both courses: 3
Python only: 1
Java only: 1
Total unique students: 5
Both: {'Alice', 'Bob', 'Tom'}
======================================
"""
enrollments = [
    ("Alice", "Python"),
    ("Bob", "Java"),
    ("Tom", "Python"),
    ("Alice", "Java"),
    ("Jack", "Java"),
    ("Bob", "Python"),
    ("Yue", "Python"),
    ("Tom", "Java"),
    ("Alice", "Python"),
    ("Jack", "Java")
]
python_students = set()
java_students = set()
for name, language in enrollments:
    if language == "Python":
        python_students.add(name)
    elif language == "Java":
        java_students.add(name)

python_count = len(python_students)
java_count = len(java_students)
both = python_students & java_students
both_count = len(both)
python_only = python_count - both_count
java_only = java_count - both_count
unique = python_count + java_count - both_count

print("===== Course Enrollment Analyzer =====")
print(f"Python students: {python_count}")
print(f"Java students: {java_count}")
print(f"Python students: {python_count}")
print(f"Both courses: {both_count}")
print(f"Python only: {python_only}")
print(f"Java only: {java_only}")
print(f"Total unique students: {unique}")
print(f"Both: {both}")
print("======================================")



