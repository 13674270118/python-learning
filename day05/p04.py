"""
网站记录了一批访问用户：
visitors = [
    "Alice",
    "Bob",
    "Alice",
    "Tom",
    "Bob",
    "Jack",
    "Alice"
]

要求输出：
Total visits: 7
Unique visitors: 4
这里：
Total visits
→ 每次访问都算
Unique visitors
→ 同一个人访问多次只算一次
"""
visitors = [
    "Alice",
    "Bob",
    "Alice",
    "Tom",
    "Bob",
    "Jack",
    "Alice"
]
total_visits = len(visitors)
unique_visits = len(set(visitors))





