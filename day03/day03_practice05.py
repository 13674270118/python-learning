"""
给定：
text = "apple,banana,orange,grape"

要求：
使用 split() 按 , 拆开
使用 join() 用 " | " 重新连接

最终：
apple | banana | orange | grape
"""
text = "apple,banana,orange,grape"
words = text.split(",")
new_text = " | ".join(words)
print(new_text)


