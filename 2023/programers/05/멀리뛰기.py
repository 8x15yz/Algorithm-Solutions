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
        print(p+q, p, q)
        print(factorial(p+q), factorial(p), factorial(q))
        print(factorial(p+q)/(factorial(p)*factorial(q)))
        p -= 1
        q += 2
        answer += factorial(p+q)/(factorial(p)*factorial(q))
    return answer%1234567



## 5월 10일 풀이 37.5점짜리 드디어 정답케이스가 일부 나오고 있긴 함
def factorial(n):
    ans = 1
    for i in range(n, 0, -1): ans *= i
    return ans

def solution(n):
    answer = 0
    PQtuple = (n//2, 1) if n%2 else (n//2, 0)
    p, q= PQtuple
    for i in range(p+1):
        answer += int(factorial(p+q)/(factorial(p)*factorial(q)))
        p -= 1
        q += 2
        
    return answer%1234567
# 이거 내가 맞출수는 있는 문제일까???????????
