class Student:
    count = 0

    def __init__(self, name):
        # 保存 name
        # 每创建一个 Student，count + 1
        self.name = name
        Student.count += 1

student1 = Student("James")
student2 = Student("Tom")
student3 = Student("Amy")

print(student1.name)
print(student2.name)
print(student3.name)

print(Student.count)