"""
让用户输入一句英文，例如：
Python is fun to learn

程序输出：
Word count: 5
"""
word = input("enter a sentence: ")
count = len(word.strip().split())
print(f"Word count: {count}")

