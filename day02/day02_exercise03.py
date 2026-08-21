"""
猜数字
假设答案固定为：
answer = 7

让用户不断猜数字：
Guess: 3
Too small
Guess: 10
Too large
Guess: 7
Correct!

规则：
guess < answer → Too small
guess > answer → Too large
guess == answer → Correct! 并结束循环
"""
target = 7
while True:
    guess = int(input("Guess: "))
    if guess < target:
        print("Too small")
    elif guess > target:
        print("Too large")
    else:
        print("Correct")
        break

