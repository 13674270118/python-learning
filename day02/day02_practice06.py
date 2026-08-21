"""
现在你自己完成
计算 1～50 中所有能被 5 整除的整数：
最后输出：
    Count: ?
    Total: ?
"""
count = 0
total = 0
for i in range(1, 51):
    if i % 5 == 0:
        count += 1
        total += i

print(f"count is {count}")
print(f"total is {total}")



