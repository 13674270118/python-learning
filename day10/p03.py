"""
完成：
def convert_number(value):
    ...

尝试：
int(value)
如果成功：
convert_number("100")

返回：
100

如果失败：
convert_number("hello")
"""
def convert_number(value):
    try:
        num = int(value)
    except ValueError as e:
        print(f"Conversion error: {e}")
        return None
    else:
        return num









