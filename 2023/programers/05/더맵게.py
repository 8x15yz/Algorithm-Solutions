#https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

def solution(scoville, K):
    answer = 0
    while True:
        scoville.sort()
        if len(scoville) < 2: return -1
        elif scoville[0] < K: 
            scoville = [scoville[0]*scoville[1]*2] + scoville[2:]
            answer += 1
        else: return answer
