"""
def calculate_average(*scores):
    ...

要求它能够接受任意数量的成绩，并返回平均分。
"""
def calculate_average(*scores):
    total = 0
    num = 0
    for score in scores:
        total += score
        num += 1
    return total / num



