# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    N, M = len(wallpaper), len(wallpaper[0])
    answer = []
    minx, miny, maxx, maxy = 999, 999, 0, 0
    for i in range(N):
        for j in range(M):
            if wallpaper[i][j] == "#" and minx > i: minx = i
            if wallpaper[N-i-1][j] == "#" and maxx < N-i: maxx = N-i
            if wallpaper[i][M-j-1] == "#" and maxy < M-j: maxy = M-j
            if wallpaper[i][j] == "#" and miny > j: miny = j
        
    return [minx, miny, maxx, maxy]
