"""
升级版猜数字游戏
程序固定：
target = 37
用户不断猜数字。

规则：
guess < target → Too small
guess > target → Too large
guess == target → Correct!

记录用户一共猜了多少次
最多只能猜 5 次
"""
target = 37
count = 0
while count < 5:
    guess = int(input("Guess: "))
    count += 1
    if guess < target:
        print("Too small")
    elif guess > target:
        print("Too large")
    else:
        print("Correct")
        print(f"You guessed {count} times.")
        break
    if count == 5:
        print("Game over!")

