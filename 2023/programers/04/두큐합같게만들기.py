# https://school.programmers.co.kr/learn/courses/30/lessons/118667
def solution(queue1, queue2):
    answer = -2
    queue = queue1+queue2
    p1, p2 = 0, 1
    half = sum(queue)//2
    while p1 < len(queue):
        sumq = 0
        if p1 > p2:
            for i in range(p1, len(queue)): sumq += queue[i]
            for i in range(p2+1): sumq += queue[i]
        else:
            for i in range(p1, p2+1): sumq += queue[i]
        if sumq == half: break
        else:
            if sumq > half: p1 += 1
            else: p2 += 1
    else:
        if sumq != half: 
            return -1
            
    print(p1%len(queue1), p2%len(queue1), sumq, half)
    return answer
