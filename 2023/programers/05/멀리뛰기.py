# https://school.programmers.co.kr/learn/courses/30/lessons/12914
# 요녀석봐라,.,?
def factorial(n):
    ans = 1
    for i in range(n, 0, -1): ans *= i
    return ans

def solution(n):
    answer = 0
    PQtuple = (n//2, 1, n//2+1) if n%2 else (n//2, 0, n//2+1)
    p, q, cnt= PQtuple
    for i in range(cnt):
        p -= 1
        q += 2
        answer += factorial(p+q)//(factorial(p)*factorial(q))
        
    return answer%1234567
