# https://school.programmers.co.kr/learn/courses/30/lessons/172928
dt = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

def solution(park, routes):
    n, m = len(park), len(park[0])
    si, sj = 0, 0
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S": 
                si, sj = i, j
                break
    
    for route in routes:
        d, sq = route.split()
        di, dj = dt[d]
        fi, fj = si, sj
        for _ in range(int(sq)):
            fi += di
            fj += dj
            if 0 <= fi < n and 0 <= fj < m and park[fi][fj] != "X": continue
            else: break
        else: si, sj = fi, fj
    
    return [si, sj]
