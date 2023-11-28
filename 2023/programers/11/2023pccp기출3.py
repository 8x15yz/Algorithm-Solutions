# https://school.programmers.co.kr/learn/courses/30/lessons/250135

def solution(h1, m1, s1, h2, m2, s2):
    answer = -1
    minute = 180/60
    hour = minute/60
    halfday = minute/720
    
    start = h1*3600+m1*60+s1
    end = h2*3600+m2*60+s2
    
    print(minute, hour, halfday)
    return answer
