# https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 이게 문제냐ㅑ ~ 10초컷

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer
