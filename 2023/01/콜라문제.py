# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    res = 0
    while n >= a:
        res = n-(n//a*a)
        answer += (n//a)*b 
        n = (n//a)*b + res
        res = 0
        
    return answer
