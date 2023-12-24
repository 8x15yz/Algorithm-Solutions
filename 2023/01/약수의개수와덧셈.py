# https://school.programmers.co.kr/learn/courses/30/lessons/77884

from math import sqrt, floor
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if sqrt(i) == floor(i**0.5):
            answer -= i
        else:
            answer += i
    return answer
