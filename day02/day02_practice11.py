"""
判断质数 Prime Number
"""
number = int(input("enter a number: "))
if number <= 1:
    print("Not Prime")
else:
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")