"""
def analyze_scores(scores):
    ...

传入：
scores = [80, 95, 70, 88, 100]

要求函数一次返回：
最高分
最低分
平均分
"""
def analyze_scores(scores):
    h = max(scores)
    l = min(scores)
    ave = sum(scores) / len(scores)
    return h, l, ave

scores = [80, 95, 70, 88, 100]
h, l, ave = analyze_scores(scores)


