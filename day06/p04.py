"""
给定：
student = {
    "name": "Alice",
    "grades": {
        "Python": 95,
        "Java": 82,
        "SQL": 88
    }
}

不修改 Dictionary，输出：
Student: Alice
Python: 95
Java: 82
SQL: 88
Average: 88.33333333333333
"""
student = {
    "name": "Alice",
    "grades": {
        "Python": 95,
        "Java": 82,
        "SQL": 88
    }
}
grade = student["grades"]
python_grade = grade["Python"]
java_grade = grade["Java"]
sql_grade = grade["SQL"]
average = (python_grade + java_grade + sql_grade) / 3

print(f'Student: {student["name"]}')
print(f'Python: {python_grade}')
print(f'Java: {java_grade}')
print(f'SQL: {sql_grade}')
print(f'Average: {average}')

