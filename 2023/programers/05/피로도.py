# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    answer = 0
    dungeons = sorted(dungeons, reverse=True)
    for dun in dungeons:
        if k >= dun[0]: 
            k -= dun[1]
            answer += 1
        else: break
        
    return answer
