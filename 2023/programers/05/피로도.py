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


# 정답코드
from itertools import permutations
def solution(k, dungeons):
    answer = []
    possible = list(permutations(dungeons, len(dungeons)))
    for pos in possible:
        hp = k
        cnt = 0
        for p in pos:
            if hp >= p[0]:
                hp -= p[1]
                cnt += 1
            else: 
                answer.append(cnt)
                break
        else: 
            answer.append(cnt)
    return max(answer)
