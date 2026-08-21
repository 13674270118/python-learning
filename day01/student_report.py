"""
Student Evaluation System
程序询问用户：
    name
    age
    score

如果 age < 18
Status → Minor
否则
Status → Adult

score >= 90 → A
score >= 80 → B
score >= 70 → C
score >= 60 → D
否则        → F

最后输出类似：
===== Student Report =====
Name: Yue
Age: 24
Status: Adult
Score: 85
Grade: B
==========================
"""
name = input("enter your name: ")
age = int(input("enter your age: "))
score = int(input("enter your score: "))
status = None
if age < 18:
    status = "Minor"
else:
    status = "Adult"

grade = None
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("====Student Report====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Status: {status}")
print(f"Score: {score}")
print(f"Grade: {grade}")
print("==========================")






