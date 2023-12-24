#https://school.programmers.co.kr/learn/courses/30/lessons/131127?language=python3

def solution(want, number, discount):
    answer = 0
    wantD = {}
    buyD = {}
    for i in range(len(want)):
        wantD[want[i]] = number[i]
        buyD[want[i]] = 0
    for i in range(len(discount)-9):
        copyD = buyD.copy()
        for sale in discount[i:i+10]:
            if sale in copyD: copyD[sale] += 1
            if copyD == wantD: answer += 1
    else: return answer
