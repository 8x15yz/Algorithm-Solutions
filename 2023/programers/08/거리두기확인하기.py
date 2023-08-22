# https://school.programmers.co.kr/learn/courses/30/lessons/81302

from itertools import combinations
dt1 = [(1, 0), (-1, 0), (0, -1), (0, 1)]
dt2 = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

def solution(places):
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]
    answer = []
    for place in places:
        Ps = []
        Xs = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P": Ps.append((i, j))
                if place[i][j] == "X": Xs.append((i, j))
        for a, b in list(combinations([i for i in range(len(Ps))], 2)):
            p1i, p1j = Ps[a]
            p2i, p2j = Ps[b]
            if abs(p1i - p2i) + abs(p1j - p2j) <= 2:
                
                ## 델타탐색 : 직선 4방향 1거리
                def recogfir(p1i, p1j, p2i, p2j):
                    for di, dj in dt1:
                        if p1i + di == p2i and p1j + dj == p2j:
                            return 0
                    else: return 1
                if recogfir(p1i, p1j, p2i, p2j) == 0:
                    answer.append(0)
                    break
                    
                ## 델타탐색 : 대각선 4방향
                def recogsec(p1i, p1j, p2i, p2j):
                    pass
                if recogsec(p1i, p1j, p2i, p2j) == 0:
                    answer.append(0)
                    break
                
                ## 델타탐색 : 직선 4방향 2거리
                def recogfin(p1i, p1j, p2i, p2j):
                    pass
                if recogfin(p1i, p1j, p2i, p2j) == 0:
                    answer.append(0)
                    break
                    
                
        print()
    return answer
