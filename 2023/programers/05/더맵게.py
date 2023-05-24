#https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

# 난장판코드
def solution(scoville, K):
    answer = 0
    while True:
        scoville.sort()
        if len(scoville) < 2: return -1
        elif scoville[0] < K: 
            scoville = [scoville[0]*scoville[1]*2] + scoville[2:]
            answer += 1
        else: return answer


# 정확성만점인데 효율성거지
def solution(scoville, K):
    answer = 0
    while len(scoville) > 1:
        scoville.sort()
        if scoville[0] >= K: return answer
        scoville = [scoville[0]+scoville[1]*2] + scoville[2:]
        answer += 1
        
    if scoville[0] < K: return -1
    else: return answer
   

