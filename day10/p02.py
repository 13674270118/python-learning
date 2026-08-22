"""
完成下面函数：
def convert_age(value):
    try:
        # 转成 int
    except ValueError:
        return None
    else:
        # 返回转换成功的整数

要求：
print(convert_age("23"))
print(convert_age("hello"))

得到：
23
None
"""
def convert_age(value):
    try:
        num = int(value)
    except ValueError:
        return None
    else:
        return num

print(convert_age("23"))
print(convert_age("hello"))



