"""
给定：
languages = ["Python", "Java", "Python", "C++", "Python", "SQL"]

程序输出：
Python found
First position: 0
Count: 3
"""
languages = ["Python", "Java", "Python", "C++", "Python", "SQL"]
if "Python" in languages:
    print("Python found")
    print(f'First position: {languages.index("Python")}')
    print(f'Count: {languages.count("Python")}')



