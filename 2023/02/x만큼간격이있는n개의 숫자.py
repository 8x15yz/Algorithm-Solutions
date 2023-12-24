# https://school.programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    answer = []
    if x == 0:
        for _ in range(n):
            answer.append(x)
    else:
        for i in range(x, x*(n+1), x):
            answer.append(i)
    return answer
