"""
给定：
scores = [88, 45, 76, 59, 93, 61, 38, 100]

要求程序自己计算并输出：
Total students: 8
Highest: 100
Lowest: 38
Average: 70.0
Pass: 5
Fail: 3
Excellent: [88, 76, 93, 100]

规定：
>= 60 → Pass
< 60  → Fail
>= 75 → Excellent

其中 Excellent 必须是一个新的 List。
"""
scores = [88, 45, 76, 59, 93, 61, 38, 100]
total_students = len(scores)
highest = max(scores)
lowest = min(scores)
average = sum(scores) / total_students
p = 0
f = 0
excellent = []
for score in scores:
    if score >= 60:
        p += 1
        if score >= 75:
            excellent.append(score)
    else:
        f += 1

print(f"Total students: {total_students}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Average: {average}")
print(f"Pass: {p}")
print(f"Fail: {f}")
print(f"Excellent: {excellent}")






