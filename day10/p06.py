"""
def load_data():
    ...

要求读取：
data/test.json

三种情况：
文件正常
→ return json.load(file)

文件不存在
→ print("File not found")
→ return {}

JSON 损坏
→ print("Invalid JSON")
→ return {}

要求使用两个不同的：
except FileNotFoundError:
和：
except json.JSONDecodeError:
"""
import json
def load_data():
    try:
        with open("data/test.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found")
        return {}
    except json.JSONDecodeError:
        print("File was break")
        return {}
    else:
        return data





