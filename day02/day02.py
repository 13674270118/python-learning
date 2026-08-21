# loop
count = 1

while count <= 5:
    print("Hello")
    count = count + 1

# 累加
# 1+2+3+4+5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1

print(total)

# 无限循环（死循环）
# i = 1
# while i <= 5:
#     print(i)

# break
i = 1
while i <= 10:
    if i == 5:
        break

    print(i)
    i += 1

# continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# for
for i in range(1,6):
    print(i)

# range()
for i in range(5):
    print(i) # 0,1,2,3,4

range(2,7) # 2,3,4,5,6

for i in range(2,11,2):
    print(i) # 2,4,6,8,10

range(5,0,-1) # 5,4,3,2,1

# 计数器
count = 0
for i in range(1,11):
    if i % 2 == 0:
        count += 1

print(i)

# nested loop
for i in range(1,4):
    for j in range(1,3):
        print(i, j)









