"""
假设有：
def start_shop():
    print("Shop started")

def show_menu():
    print("1. View products")
    print("2. Sell product")

请你补成一个完整的 main.py。
要求：
① 创建
def main():

在里面依次调用：
start_shop()
show_menu()
② 最后必须使用
if __name__ == "__main__":
调用 main()。

直接运行后：
Shop started
1. View products
2. Sell product
"""
def start_shop():
    print("Shop started")

def show_menu():
    print("1. View products")
    print("2. Sell product")

def main():
    start_shop()
    show_menu()

if __name__ == "__main__":
    main()




