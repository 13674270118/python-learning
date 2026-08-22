"""
现在已经有：
data/products.txt
内容：
apple - Price: 5, Stock: 10
mac - Price: 1000, Stock: 3

写代码：
使用 "r" 打开文件
使用 read() 读取全部内容
保存到变量 content
关闭文件
打印 content
打印 content 的数据类型

预期最后类似：
apple - Price: 5, Stock: 10
mac - Price: 1000, Stock: 3
<class 'str'>
"""
file = open("data/products.txt", "r")
content = file.read()
file.close()
print(content)
print(type(content))



