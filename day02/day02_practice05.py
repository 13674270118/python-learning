"""
使用 for，计算：
1～100 中，有多少个整数能被 7 整除？
"""
count = 0
for i in range(1,101):
    if i % 7 == 0:
        count += 1

print(count)
