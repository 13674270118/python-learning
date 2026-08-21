"""
用户输入任意一句话，统计其中的元音字母数量(a e i o u)

例如：
Enter something: Hello Python
Vowels: 3
"""
words = input("enter something: ")
new_word = words.strip().lower()
count = 0
for i in new_word:
    if i in "aeiou":
        count += 1
print(count)



