"""
给定：
languages = {"Python", "Java", "C++"}

依次：
添加 "SQL"
再添加一次 "Python"
删除 "Java"
尝试删除一个不存在的 "Go"，但程序不能报错
输出最终 Set
"""
languages = {"Python", "Java", "C++"}
languages.add("SQL")
languages.add("Python")
languages.remove("Java")
languages.discard("Go")
print(languages)



