# https://school.programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    format = ['1', '2', '4']
    
    while n > 0:
        n -= 1
        answer = format[n%3] + answer
        n //= 3
    return answer
