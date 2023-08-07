# https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    line1 = [dots[0]]
    line2 = [dots[0]]
    for i in range(1, 4):
        if dots[0][1] == dots[i][1]:
            line1.append(dots[i])
        elif dots[0][0] == dots[i][0]: 
            line2.append(dots[i])
    return abs(line1[0][0]-line1[1][0])*abs(line2[0][1]-line2[1][1])
            
