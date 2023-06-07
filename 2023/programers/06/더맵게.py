#https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)
    while scoville[0] < K:
        if len(scoville) == 1: 
            if scoville[0] < K: answer = -1
            break
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a+b*2)
            answer += 1
    return answer
  
  
  

