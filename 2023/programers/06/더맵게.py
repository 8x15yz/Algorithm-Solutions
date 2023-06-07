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
  
  
  
# 구현중 ..
import heapq
def heapPop(heap):
    if len(heap) <= 2:
        return 0, heap
    minval = heap[1]
    heap[1] = heap.pop()
    i = 1
    while True:
        if len(heap) <= 2:
            break
        elif len(heap) == 3:
            if heap[1] > heap[2]:
                heap[1], heap[2] = heap[2], heap[1]
            break
        elif len(heap) >= 4:
            if i*2 > len(heap) or heap[i] < min(heap[i*2], heap[i*2+1]):
                break
            else:
                if heap[i*2] > heap[i*2+1]:
                    heap[i*2+1], heap[i] = heap[i], heap[i*2+1]
                    i = i*2+1
                else:
                    heap[i*2], heap[i] = heap[i], heap[i*2]
                    i = i*2

    return minval, heap

def heapPush(scoville, val):
    return scoville

def solution(scoville, K):
    answer = 0
    scoville += [0]
    scoville = sorted(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1: 
            if scoville[0] < K: return -1
            else: return answer
        else:
            a, scoville = heapPop(scoville)
            b, scoville = heapPop(scoville)
            # scoville = heapPush(scoville, a+b*2)
            heapq.heappush(scoville, a+b*2)
            answer += 1
    return answer
