# https://school.programmers.co.kr/learn/courses/30/lessons/81302

# 이렇게 허술한 코드가 83점?????????
from itertools import combinations
dt1 = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def solution(places):
    #places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]
    answer = []
    for place in places:
        Ps = []
        Xs = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P": Ps.append((i, j))
                if place[i][j] == "X": Xs.append((i, j))
        for a, b in list(combinations([i for i in range(len(Ps))], 2)):
            #print(a, b)
            p1i, p1j = Ps[a]
            p2i, p2j = Ps[b]
            if abs(p1i - p2i) + abs(p1j - p2j) <= 2:
                

                def recogfir(p1i, p1j, p2i, p2j):
                    for di, dj in dt1:
                        if p1i + di == p2i and p1j + dj == p2j:
                            return 0 
                        elif p1i + 2*di == p2i and p1j + 2*dj == p2j:
                            if place[p1i+di][p1j+dj] == "O":
                                return 0
                    else: return 1
                if recogfir(p1i, p1j, p2i, p2j) == 0:
                    answer.append(0)
                    break
                    
                def recogsec(p1i, p1j, p2i, p2j):
                    if p1i + 1 == p2i and p1j + 1 == p2j:
                        if place[p1i+1][p1j] == "O" or place[p1i][p1j+1] == "O":
                            return 0
                    else: return 1
                if recogsec(p1i, p1j, p2i, p2j) == 0:
                    answer.append(0)
                    break
        else: answer.append(1)
    return answer
