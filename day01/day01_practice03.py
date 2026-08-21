"""
用户输入：
    age
    score
规则：
    age >= 18 并且 score >= 60 → 输出 "Qualified"
    否则 → 输出 "Not qualified"

age = 20
score = 75
→ Qualified

age = 17
score = 90
→ Not qualified
"""
age = int(input("enter your age: "))
score = int(input("enter your score: "))
if age >= 18 and score >= 60:
    print("Qualified")
else:
    print("Not qualified")

