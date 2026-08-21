"""
假设有网站用户访问记录：
visits = [
    ("Alice", "Python"),
    ("Bob", "Java"),
    ("Alice", "Java"),
    ("Tom", "Python"),
    ("Bob", "Python"),
    ("Jack", "Java"),
    ("Alice", "Python")
]

分析这些数据，最后得到两个 Set：
python_users = set()
java_users = set()
最终计算并输出：
Python users: 3
Java users: 3
Both: {'Alice', 'Bob'}
Total unique users: 4
"""
visits = [
    ("Alice", "Python"),
    ("Bob", "Java"),
    ("Alice", "Java"),
    ("Tom", "Python"),
    ("Bob", "Python"),
    ("Jack", "Java"),
    ("Alice", "Python")
]
python_users = set()
java_users = set()

for name, language in visits:
    if language == "Python":
        python_users.add(name)
    elif language == "Java":
        java_users.add(name)

python_count = len(python_users)
java_count = len(java_users)
both = python_users & java_users
unique = python_count + java_count - len(both)

print(f"Python users: {python_count}")
print(f"Java users: {java_count}")
print(f"Both: {both}")
print(f"Total unique users: {unique}")






