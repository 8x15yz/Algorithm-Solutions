## https://school.programmers.co.kr/learn/courses/30/lessons/42583

## 이렇게 풀긴 했는데 너무 메모리를 많이 쓰는 기분
def solution(bridge_length, weight, truck_weights):
    truck_weights += [23]
    answer = 0
    time = [[] for _ in range(len(truck_weights)*bridge_length)]
    start = 0
    poped = truck_weights.pop(0)
    
    while truck_weights:
        for i in range(bridge_length):
            if sum(time[start+i]) + poped <= weight: 
                time[start+i].append(poped)
            else: 
                start += 1
                break
        else:
            poped = truck_weights.pop(0)
            start += 1

    for i in range(len(time)):
        if time[i] == []: return i+1


## 이뿌게 고치기
def solution(bridge_length, weight, truck_weights):

    time = [[] for _ in range(len(truck_weights)*bridge_length)]
    start, now = -1, 0
    
    while now < len(truck_weights):
        start += 1
        for i in range(bridge_length):
            if sum(time[start+i]) + truck_weights[now] <= weight: 
                time[start+i].append(truck_weights[now])
            else: break
        else: now += 1

    for i in range(len(time)):
        if time[i] == []: return i+1
    return len(time)+1
