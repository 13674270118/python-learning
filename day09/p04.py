"""
写一个函数：
def save_sale(name, quantity, total):
    ...

要求使用：
data/sales.txt和："a"

每调用一次就在文件末尾增加：
商品名,数量,总价

然后连续调用：
save_sale("apple", 3, 15)
save_sale("mac", 1, 1000)
save_sale("apple", 2, 10)

最终 sales.txt 应该是：
apple,3,15
mac,1,1000
apple,2,10
"""
def save_sale(name, quantity, total):
    with open("data/sales.txt", "a") as file:
        file.write(f"{name},{quantity},{total}\n")

save_sale("apple", 3, 15)
save_sale("mac", 1, 1000)
save_sale("apple", 2, 10)




