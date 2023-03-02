# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 당연히틀리죠?
def solution(n):
    answer = 0
    for i in range(n):
        su = 0
        for j in range(i, n):
            if su == n:
                answer += 1
                break
            su += j
    return answer
