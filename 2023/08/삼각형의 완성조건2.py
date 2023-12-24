#https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 너무쉬워서 커밋하는것도 부끄럽다
def solution(sides):
    answer = 0
    xS, nS = max(sides), min(sides)
    for i in range(1, sum(sides)):
        if i+nS <= xS: continue
        else: answer += 1
            
    return answer
