# list
li = ["python", "java", "c++", "javascript", "sql"]
print(li)
print(f"Number of languages: {len(li)}")

# List 索引
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[::-1])

# 修改 List
scores = [85, 60, 92, 70, 88]
scores[1] = 90
scores[-1] = 95
print(scores)

# append() / insert()
languages = ["Python", "Java"]
languages.insert(1, "C++")
languages.append("SQL")
languages.append("JavaScript")
print(languages)

# 删除 List 元素
languages = ["Python", "Java", "C++", "SQL"]
languages.remove("Java") # ['Python', 'C++', 'SQL']

languages = ["Python", "Java", "C++", "SQL"]
languages.pop(1) # ['Python', 'C++', 'SQL']
languages.pop() # 默认删除最后一个元素

# 查找 List 元素
names = ["Alice", "Bob", "Tom"]
print("Bob" in names) # True
print(names.index("Bob")) # 1

numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2)) # 3

# List 数值计算
scores = [85, 92, 78, 66, 95]
len(scores) # 长度
sum(scores) # 总和
max(scores) # 最大值
min(scores) # 最小值
average = sum(scores) / len(scores) # 平均值

# List 排序 sort() / reverse()
scores = [88, 76, 95, 67, 82, 91]
scores.sort() # 从小到大
scores.sort(reverse=True) # 从大到小

scores.reverse() # 反转当前顺序

# 二维 List
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Tom", 78]
]
for student in students:
    print(student)

for student in students:
    print(student[0], student[1])




