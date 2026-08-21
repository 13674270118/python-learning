"""
给定：
user = {
    "name": "Alice",
    "age": 20,
    "email": "alice@test.com",
    "password": "123456"
}

要求：
使用 pop() 删除 "password"，并把被删除的密码保存到 deleted
使用 del 删除 "age"
输出最终 user
输出：
Deleted password: 123456
"""
user = {
    "name": "Alice",
    "age": 20,
    "email": "alice@test.com",
    "password": "123456"
}

deleted = user.pop("password")
del user["age"]
print(f"Deleted password: {deleted}")



