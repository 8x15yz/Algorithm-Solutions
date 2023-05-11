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
