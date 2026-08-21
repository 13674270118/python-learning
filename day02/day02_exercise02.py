"""
让用户不断输入整数
Enter a number: 10
Enter a number: 20
Enter a number: 5
Enter a number: 0

规则：
用户可以输入任意数量的整数，当输入 0 时停止。
最后输出之前所有数字的总和：
Total: 35
"""
total = 0
while True:
    number = int(input("enter a number: "))
    if number == 0:
        break
    else:
        total += number


