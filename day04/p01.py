"""
给定：
fruits = ["apple", "banana", "orange", "grape", "watermelon"]

完成：
使用 remove() 删除 "banana"
使用 pop() 删除 "orange"（注意删除 "banana" 后索引已经发生变化）
使用 pop() 删除最后一个元素，并把被删除的值保存到 deleted
输出 fruits
输出：
Deleted: watermelon
"""
fruits = ["apple", "banana", "orange", "grape", "watermelon"]
fruits.remove("banana")
fruits.pop(1)
deleted = fruits.pop()
print(fruits)
print(f"Deleted: {deleted}")



