"""
给定：
students = [
    {
        "name": "Alice",
        "grades": {
            "Python": 95,
            "Java": 88
        }
    },
    {
        "name": "Bob",
        "grades": {
            "Python": 72,
            "Java": 65
        }
    },
    {
        "name": "Tom",
        "grades": {
            "Python": 58,
            "Java": 61
        }
    },
    {
        "name": "Jack",
        "grades": {
            "Python": 90,
            "Java": 92
        }
    }
]

你的任务是遍历所有学生，计算每个学生两门课的平均分。
规定：
average >= 60 → Pass
average < 60  → Fail
average >= 85 → Excellent

最终输出：
Alice: 91.5 - Pass
Bob: 68.5 - Pass
Tom: 59.5 - Fail
Jack: 91.0 - Pass

Pass: 3
Fail: 1
Excellent: ['Alice', 'Jack']
"""
students = [
    {
        "name": "Alice",
        "grades": {
            "Python": 95,
            "Java": 88
        }
    },
    {
        "name": "Bob",
        "grades": {
            "Python": 72,
            "Java": 65
        }
    },
    {
        "name": "Tom",
        "grades": {
            "Python": 58,
            "Java": 61
        }
    },
    {
        "name": "Jack",
        "grades": {
            "Python": 90,
            "Java": 92
        }
    }
]

pass_count = 0
fail_count = 0
excellent = []
for student in students:
    grades = student["grades"]
    average = sum(grades.values()) / len(grades.values())
    if average >= 60:
        print(f"{student['name']}: {average} - Pass")
        pass_count += 1
        if average >= 85:
            excellent.append(student["name"])
    else:
        print(f"{student['name']}: {average} - Fail")
        fail_count += 1

print(f"Pass: {pass_count}")
print(f"Fail: {fail_count}")
print(f"Excellent: {excellent}")


