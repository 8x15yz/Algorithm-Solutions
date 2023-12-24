# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    bud = 0
    for i in range(count):
        bud += price*(i+1)
    answer = bud - money
    if answer < 0:
        answer = 0
    return answer
