"""
给定：
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Tom", 58),
    ("Jack", 76)
]

要求使用 Tuple unpacking + for 输出：
Alice: Pass
Bob: Pass
Tom: Fail
Jack: Pass

规定：
score >= 60 → Pass
"""
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Tom", 58),
    ("Jack", 76)
]
for name, score in students:
    if score >= 60:
        print(f"{name}: Pass")
    else:
        print(f"{name}: Fail")





