"""
Student Management System
程序启动：
===== Student Management System =====
1. Add student
2. View students
3. Search student
4. Statistics
5. Exit
Choose:
用户可以不断选择功能。

功能 1：Add student

用户输入：
Name: Alice
Python score: 95
Java score: 88

保存成：
{
    "name": "Alice",
    "grades": {
        "Python": 95,
        "Java": 88
    }
}
然后：
students.append(...)

可以继续添加：
Bob
Tom
Jack
...

功能 2：View students
假设已经有：
Alice 95 88
Bob   72 65

输出：
===== Students =====
Alice - Python: 95, Java: 88
Bob - Python: 72, Java: 65

功能 3：Search student
用户输入：
Enter name: Alice

找到：
Name: Alice
Python: 95
Java: 88
Average: 91.5

如果不存在：
Student not found

功能 4：Statistics
假设当前：
Alice → 95, 88
Bob   → 72, 65
Tom   → 58, 61

输出：
===== Statistics =====
Students: 3
Pass: 2
Fail: 1
Excellent: 1

规定仍然是：
平均分 >= 60 → Pass
平均分 < 60  → Fail
平均分 >= 85 → Excellent

如果还没有学生：
No students

功能 5：Exit
选择：
5

输出：
Goodbye!
结束程序。
"""
students = []
while True:
    print("===== Student Management System =====")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Statistics")
    print("5. Exit")
    choice = int(input("Choose: "))

    if choice == 5:
        print("Goodbye!")
        break
    elif choice == 1:
        name = input("Name: ")
        python_score = int(input("Python score: "))
        java_score = int(input("Java score: "))
        student = {
            "name": name,
            "grade": {
                "Python": python_score,
                "Java": java_score
            }
        }
        students.append(student)
    elif choice == 2:
        if len(students) == 0:
            print("No student")
        else:
            print("===== Students =====")
            for student in students:
                name = student["name"]
                python_grade = student["grade"]["Python"]
                java_grade = student["grade"]["Java"]
                print(f"{name} - Python: {python_grade}, Java: {java_grade}")
    elif choice == 3:
        name = input("Enter name: ")
        has_student = False
        if len(students) == 0:
            print("No student")
        else:
            for student in students:
                if student["name"] == name:
                    has_student = True
                    python_grade = student["grade"]["Python"]
                    java_grade = student["grade"]["Java"]
                    average = sum(student["grade"].values()) / len(student["grade"])
                    print(f"Name: {name}")
                    print(f"Python: {python_grade}")
                    print(f"Java: {java_grade}")
                    print(f"Average: {average}")

            if has_student == False:
                print("Student not found")
    elif choice == 4:
        pass_count = 0
        fail_count = 0
        excellent_count = 0
        if len(students) == 0:
            print("No student")
        else:
            for student in students:
                average = sum(student["grade"].values()) / len(student["grade"])
                if average >= 60:
                    pass_count += 1
                    if average >= 85:
                        excellent_count += 1
                else:
                    fail_count += 1
            print("===== Statistics =====")
            print(f"Students: {len(students)}")
            print(f"Pass: {pass_count}")
            print(f"Fail: {fail_count}")
            print(f"Excellent: {excellent_count}")









