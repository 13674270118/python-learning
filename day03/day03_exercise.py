"""
用户输入任意文本，例如：
Hello Python 123!

程序需要统计并输出：
Characters: 17
Letters: 11
Digits: 3
Spaces: 2
Vowels: 3
Other: 1
"""
word = input("enter something: ")
char_count = len(word)
letter_count = 0
digit_count = 0
space_count = 0
vowel_count = 0
other_count = 0
for i in word.lower():
    if i in "aeiou":
        letter_count += 1
        vowel_count += 1
    elif i.isalpha():
        letter_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i.isspace():
        space_count += 1
    else:
        other_count += 1




