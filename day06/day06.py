# Dictionary 基础
student = {
    "name": "Yue",
    "age": 24,
    "major": "Mathematics",
    "score": 95
}
data = {}
data = dict()

# 读取 Dictionary 数据
student = {
    "name": "Yue",
    "age": 24,
    "major": "Mathematics",
    "score": 95
}
print(student["name"])

# get() 安全读取
student = {
    "name": "Yue",
    "score": 95
}

student.get("email") # None
student.get("email", "Not provided") # Not provided

# 添加和修改 Dictionary
student = {
    "name": "Yue",
    "score": 95
}

student["score"] = 98
student["major"] = "Mathematics"

# 删除 Dictionary 数据
student = {
    "name": "Yue",
    "age": 24,
    "score": 95
}

deleted = student.pop("age")
del student["age"]

# in 判断 Key
student = {
    "name": "Alice",
    "score": 95
}

print("name" in student) # True

# keys() / values() / items()
student = {
    "name": "Alice",
    "age": 20,
    "score": 95
}

print(student.keys()) # name, age, score
print(student.values()) # Alice, 20, 95

for key, value in student.items():
    print(key, value)








