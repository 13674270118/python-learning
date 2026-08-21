"""
用户输入任意字符串，例如：
Hello Python

统计其中有多少个字母 "o"。
要求忽略大小写，所以：
Hello
HELLO
hello
里面的 o / O 都应该统计。
"""
text = input("enter something: ")
new_text = text.strip().upper()
count = 0
for i in new_text:
    if i == "O":
        count += 1

print(count)




