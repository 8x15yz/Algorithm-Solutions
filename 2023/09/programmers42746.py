## https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 시간초과 
from itertools import permutations
def solution(numbers):
    answer = []
    for case in list(permutations(numbers, len(numbers))):
        ca = ''
        for c in case: ca += str(c)
        answer.append(int(ca))
        
    return str(max(answer))


# 정해
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (x * 4)[:4], reverse = True)
    return str(int("".join(numbers)))
