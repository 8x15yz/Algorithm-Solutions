# 의외로 쉬웠음 헐 ~
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    serial = [0 for _ in range(12)]
    for i in range(4):
        for j in range(3):
            serial[(3*(i+1)-j)-1] = (i, j)
    answer = ''
    tL, tR = 10, 12
    
    for id in numbers:
        if id == 0:
            id = 11
        if id == 1 or id == 4 or id == 7:
            answer += 'L'
            tL = id
        elif id == 3 or id == 6 or id == 9:
            answer += 'R'
            tR = id
        else:
            # 거리가 같다면 : answer+= upper(hand[0])
            routeR = abs(serial[id-1][0]-serial[tR-1][0])+abs(serial[id-1][1]-serial[tR-1][1])
            routeL = abs(serial[id-1][0]-serial[tL-1][0])+abs(serial[id-1][1]-serial[tL-1][1])
            if routeR > routeL:
                answer += 'L'
                tL = id
            elif routeR < routeL:
                answer += 'R'
                tR = id
            else:
                if hand == 'right':
                    answer += 'R'
                    tR = id
                else:
                    answer += 'L'
                    tL = id
            
    return answer
