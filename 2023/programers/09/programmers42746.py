## https://school.programmers.co.kr/learn/courses/30/lessons/42746
## 밑장빼기 할라다가 딱 걸려브러 ..

from itertools import permutations
def solution(numbers):
    answer = []
    for case in list(permutations(numbers, len(numbers))):
        ca = ''
        for c in case: ca += str(c)
        answer.append(int(ca))
        
    return str(max(answer))
