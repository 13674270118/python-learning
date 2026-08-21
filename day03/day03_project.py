"""
String Analyzer
用户输入：
Enter text: Hello Python 123!

程序输出：
===== String Analyzer =====
Original: Hello Python 123!
Length: 17
Words: 3
Letters: 11
Digits: 3
Spaces: 2
Vowels: 3
Other: 1
Uppercase: HELLO PYTHON 123!
Lowercase: hello python 123!
Reversed: !321 nohtyP olleH
===========================
"""
text = input("enter text: ")
original = text
length = len(text)
words = len(text.split())
letter_count = 0
digit_count = 0
space_count = 0
vowel_count = 0
other_count = 0

for i in text.lower():
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

print("===== String Analyzer =====")
print(f"Original: {original}")
print(f"Length: {length}")
print(f"Words: {words}")
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Vowels: {vowel_count}")
print(f"Other: {other_count}")
print(f"Uppercase: {original.upper()}")
print(f"Lowercase: {original.lower()}")
print(f"Reversed: {original[::-1]}")
print("===========================")


