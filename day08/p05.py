"""
def register_student(name, age, major):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major}")
① 使用 list
student1 = ["James", 23, "Mathematics"]

要求只写一行调用：
register_student(???)

② 使用 dictionary
student2 = {
    "name": "Tom",
    "age": 24,
    "major": "Computer Science"
}
"""
def register_student(name, age, major):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major}")

student1 = ["James", 23, "Mathematics"]
register_student(*student1)

student2 = {
    "name": "Tom",
    "age": 24,
    "major": "Computer Science"
}
register_student(**student2)
