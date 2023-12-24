# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 이터툴즈 짱
from itertools import combinations

def solution(nums):
    answer = 0
    for comset in list(combinations(nums, 3)):
        for s in range(2, sum(comset)):
            if sum(comset) % s == 0:
                break
        else:
            answer += 1
                
    return answer
