"""
用户输入：
Hello 123!

遍历这个字符串，分别统计：
Letters: 5
Digits: 3
Spaces: 1
! 暂时什么都不做。
"""
words = input("enter something: ")
count_l = 0
count_d = 0
count_s = 0
for i in words:
    if i.isalpha():
        count_l += 1
    elif i.isdigit():
        count_d += 1
    elif i.isspace():
        count_s += 1

print(f"Letters: {count_l}")
print(f"Digits: {count_d}")
print(f"Spaces: {count_s}")




