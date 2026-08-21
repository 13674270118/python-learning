"""
使用两个 for 循环输出：
*****
****
***
**
*
"""
for i in range(1, 6):
    for j in range(1, 7 - i):
        print("*", end="")
    print()