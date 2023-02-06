#https://school.programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    answer = ''
    s = 0
    month = [0,31,29,31,30,31,30,
             31,31,30,31,30,31]
    week = ['THU', 'FRI','SAT', 'SUN','MON','TUE','WED']
    for i in range(a-1, 0, -1):
        s += month[i]
    answer = week[(s+b)%7]
    return answer
