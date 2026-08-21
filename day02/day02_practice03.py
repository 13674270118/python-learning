"""
使用 for + range() 计算：
1 + 3 + 5 + 7 + ... + 99
1～100 中所有奇数的总和
"""
total = 0
for i in range(1,100,2):
    total += i

print(total)



