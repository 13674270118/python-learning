"""
FizzBuzz
遍历 1～30：
    能被 3 和 5 同时整除 → 输出 "FizzBuzz"
    只能被 3 整除 → 输出 "Fizz"
    只能被 5 整除 → 输出 "Buzz"
    都不能 → 输出数字本身
"""
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


