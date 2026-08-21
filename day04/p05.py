"""
给定：
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Tom", 58]
]

使用 for 遍历，输出：
Alice: Pass
Bob: Pass
Tom: Fail

规定：
score >= 60 → Pass
"""
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Tom", 58]
]
for student in students:
    if student[1] >= 60:
        print(f'{student[0]}: Pass')
    else:
        print(f'{student[0]}: Fail')









