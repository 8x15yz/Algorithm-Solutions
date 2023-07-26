#https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations

def solution(expression):
    calset = list(permutations(["+", "-", "*"], 3))
    answer = 0
    num = ""
    pblm = []
    
    for e in expression:
        if not e.isdigit():
            pblm.append(int(num))
            pblm.append(e)
            num = ""
        else:
            num += e
    else: pblm.append(int(num))
    
    print(pblm)
    return answer
