"""
给定：
scores = [88, 76, 95, 67, 82, 91]

要求输出：
Students: 6
Highest: 95
Lowest: 67
Total: 499
Average: 83.16666666666667
"""
scores = [88, 76, 95, 67, 82, 91]
students = len(scores)
highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / students

print(f"Students: {students}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Total: {total}")
print(f"Average: {average}")



