# https://school.programmers.co.kr/learn/courses/30/lessons/138476#

from itertools import combinations
def solution(k, tangerine):
    answer = 0
    tGD = [0 for _ in range(max(tangerine))]
    for i in tangerine: tGD[i-1] += 1
    
    i, flag = 1, True
    while flag:
        tCList = list(combinations(tGD, i))
        for tC in tCList:
            if sum(tC) >= k: 
                answer = len(tC)
                flag = False
                break
        else: i += 1
    
    return answer




## 람다함수써보기 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 구질구질하다
from itertools import combinations
def solution(k, tangerine):
    answer = 0
    tGD = [0 for _ in range(max(tangerine))]
    for i in tangerine: tGD[i-1] += 1
    
    i = 1
    while True:
        tCList = list(map(lambda x: sum(x), list(combinations(tGD, i))))
        if k <= max(tCList): return i
        else: i += 1
    
    return answer


## 다른 시도
from itertools import combinations
def solution(k, tangerine):
    answer = 0
    tGD = [0 for _ in range(max(tangerine))]
    for i in tangerine: tGD[i-1] += 1
    tGD = sorted(tGD, reverse=True)
    for i in range(len(tGD)):
        if sum(tGD[:i]) >= k:
            answer = i
            break
    return answer


### 예외처리 시작
from itertools import combinations
def solution(k, tangerine):
    answer = 0
    tGD = [0 for _ in range(max(tangerine))]
    for i in tangerine: tGD[i-1] += 1
    if max(tGD) >= k: return 1
    else:
        tGD = sorted(tGD, reverse=True)
        for i in range(len(tGD)):
            if sum(tGD[:i]) >= k:
                return i
