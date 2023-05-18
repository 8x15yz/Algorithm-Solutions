#https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3

def solution(pri, location):
    answer = 1
    priorities = []
    for i in range(len(pri)):
        priorities.append((i, pri[i]))
        
    while True:
        i, poped = priorities.pop(0)
        if poped >= max(pri):
            pri.remove(poped)
            if i == location: return answer
            else: answer += 1
        else: priorities.append((i, poped))
