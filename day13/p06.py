class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, major):
        # 使用 super()
        # 初始化 name 和 age
        super().__init__(name, age)
        # Student 自己初始化 major
        self.major = major

student = Student("James", 23, "Mathematics")

print(student.name)
print(student.age)
print(student.major)

