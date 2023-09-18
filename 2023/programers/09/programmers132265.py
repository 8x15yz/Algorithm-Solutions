# https://school.programmers.co.kr/learn/courses/30/lessons/132265

## 카운터 디박이다 ....
from collections import Counter
def solution(topping):
    answer = 0
    cheolSu = Counter(topping)
    dongSaeng = {}
    while topping:
        poped = topping.pop()
        if poped not in dongSaeng: dongSaeng[poped] = 1
        else: dongSaeng[poped] += 1
        cheolSu[poped] -= 1
        if cheolSu[poped] == 0: del cheolSu[poped]
        if len(cheolSu) == len(dongSaeng): answer += 1
    return answer
