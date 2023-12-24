# https://school.programmers.co.kr/learn/courses/30/lessons/42890



## 0911 아무렇게나 짠 코드
from itertools import combinations
def solution(relation):
    comb = [x for x in range(1, len(relation[0]))]
    answer = 0
    for i in range(2, len(relation)):
        for unit in list(combinations(comb, i)):
            candidate = set()
            for rel in relation:
                case = ""
                for j in range(i):
                    case += rel[unit[j]]
                candidate.add(case)
            if len(candidate) == len(relation): return i
    # return answer


## 0912 정답코드
from itertools import combinations
def solution(relation):
    candiMini = []
    for i in range(1, len(relation[0])):
        units = list(combinations([i for i in range(len(relation[0]))], i))
        print(units)
        for unit in units:
            only = set()
            for rel in relation:
                key = ""
                for uni in unit: key += rel[uni]
                only.add(key)
            if len(only) == len(relation): ## 유일성검사 통과
                isMini = 0
                if candiMini == []: candiMini.append(unit)
                for candi in candiMini:
                    if not set(candi).issubset(set(unit)) and not unit in candiMini: isMini += 1
                if isMini == len(candiMini): candiMini.append(unit) ## 최소성검사 통과

    return 1 if len(candiMini) == 0 else len(candiMini)
