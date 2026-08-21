"""
计算 1 + 2 + 3 + ... + 100
"""
i = 1
total = 0
while i <= 100:
    total += i
    i += 1

print(total)

"""
计算 1～100 中所有偶数的和
"""
i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1

print(total)




