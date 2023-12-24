# https://school.programmers.co.kr/learn/courses/30/lessons/12914

# 틀린 코드
def factorial(number):
    factorialanswer = 1
    for i in range(number, 0, -1):
        factorialanswer *= i
    return factorialanswer

def solution(n):
    answer = 0
    # 이거 같은 것이 있는 순열문제 공식 적용하면 됨
    if n%2 == 0:
        for i in range(n//2+1):
            p, q = (n//2-i), (i*2)
            ppq = p+q
            a = factorial(ppq)/(factorial(p)*factorial(q))
            answer += a
    else:
        for i in range(n//2+1):
            p, q = (n//2-i)+1, (i*2)
            ppq = p+q
            a = factorial(ppq)/(factorial(p)*factorial(q))
            answer += a
            
    return answer
