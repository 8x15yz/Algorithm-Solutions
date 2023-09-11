# https://school.programmers.co.kr/learn/courses/30/lessons/42890
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
