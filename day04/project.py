"""
项目要求
首先创建一个空 List：
scores = []
然后让用户不断输入成绩：
Enter score (-1 to finish): 85
Enter score (-1 to finish): 92
Enter score (-1 to finish): 58
Enter score (-1 to finish): 76
Enter score (-1 to finish): -1

其中：
-1 → 停止输入
所有正常成绩都要保存进：
scores
输入结束后，程序输出报告：
===== Score Report =====
Scores: [85, 92, 58, 76]
Students: 4
Highest: 92
Lowest: 58
Average: 77.75
Pass: 3
Fail: 1
Excellent: [85, 92, 76]
Ascending: [58, 76, 85, 92]
========================

规定：
score >= 60 → Pass
score < 60  → Fail
score >= 75 → Excellent
"""
scores = []
while True:
    score = int(input("Enter score (-1 to finish): "))
    if score == -1:
        break
    else:
        scores.append(score)

students = len(scores)
if students == 0:
    print("No scores entered")
else:
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / students
    pass_count = 0
    fail_count = 0
    excellent = []
    for score in scores:
        if score >= 60:
            pass_count += 1
            if score >= 75:
                excellent.append(score)
        else:
            fail_count += 1
    ascending_scores = scores.copy()
    ascending_scores.sort()

    print("===== Score Report =====")
    print(f"Scores: {scores}")
    print(f"Students: {students}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Average: {average}")
    print(f"Pass: {pass_count}")
    print(f"Fail: {fail_count}")
    print(f"Excellent: {excellent}")
    print(f"Ascending: {ascending_scores}")
    print("========================")








