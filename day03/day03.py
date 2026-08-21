# 字符串与 len()
word = "python"
print(len(word))

text = "HelloPython"
print(text[:5]) # Hello
print(text[5:]) # Python
print(text[::-1]) # nohtyPolleH

# str method
text = "HelloPython"
text.upper() # HELLO PYTHON
text.lower() # hello python
"python".capitalize() # Python
"hello python".title() # Hello Python
name = "   yue   "
print(name.strip()) # yue

text = "I love Python"
print("Python" in text) # True
print("Java" in text) # False

text = "Hello Python"
print(text.find("Python")) # 6
print(text.find("Java")) # -1

filename = "report.pdf"
print(filename.startswith("report")) # True
print(filename.endswith(".pdf")) # True

text = "I like Java"
new_text = text.replace("Java", "Python")
print(new_text) # I like Python

text = "cat cat cat"
print(text.replace("cat", "dog")) # dog dog dog

text = "apple,banana,orange"
result = text.split(",")
print(result) # ['apple', 'banana', 'orange']

# 遍历字符串
word = "python"
for char in word:
    print(char)

# 字符类型判断
# 判断字母
"A".isalpha() # True
"7".isalpha() # False

# 判断数字
"A".isdigit() # False
"7".isdigit() # True

# 判断字母或数字
"A".isalnum() # True
"7".isalnum() # True
"!".isalnum() # False

# 判断空白
" ".isspace() # True




