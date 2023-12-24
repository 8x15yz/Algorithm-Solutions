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


## 그냥 푸는것도 되긴함 ..
def solution(topping):
    answer = 0
    cheolSu = {}
    for i in topping:
        if i not in cheolSu: cheolSu[i] = 1
        else: cheolSu[i] += 1

    dongSaeng = {}
    for i in topping:
        if i not in dongSaeng: dongSaeng[i] = 1
        else: dongSaeng[i] += 1
        
        if cheolSu[i] == 1: del cheolSu[i]
        else: cheolSu[i] -= 1
        
        if len(dongSaeng) == len(cheolSu):
            answer += 1
    return answer
