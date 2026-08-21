"""
用户输入一个文件名，例如：
homework.py

要求：
先使用 strip() 去掉左右空格
如果文件名以 .py 结尾 → 输出 "Python file"
否则 → 输出 "Not a Python file"

注意最好让：
HOMEWORK.PY
也能识别成 Python 文件。
"""
file_name = input("enter your file name: ")
file_name = file_name.strip().upper()
if file_name.endswith(".PY"):
    print("Python file")
else:
    print("Not a Python file")




