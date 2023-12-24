# https://school.programmers.co.kr/learn/courses/30/lessons/62048?language=python3
import math
def solution(w,h):
    answer = w*h
    square = [[0 for _ in range(w)] for _ in range(h+1)]
    inclination = h/w
    cnt = 0
    info = []
    for i in range(0, w+1): info.append(inclination*i)
    for i in range(w):
        # print(i, math.floor(info[i]), round(info[i+1]+0.1)-1)
        if math.floor(info[i]) == round(info[i+1]+0.1)-1:
            cnt += 1
        else: cnt += 2
        # square[round(info[i+1]+0.1)-1][i] = 1
        # square[math.floor(info[i])][i] = 1
    return answer-cnt
