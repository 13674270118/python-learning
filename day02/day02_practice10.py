"""
寻找因数
"""
number = int(input("enter a number: "))
for i in range(1, number+1):
    if number % i == 0:
        print(i)

