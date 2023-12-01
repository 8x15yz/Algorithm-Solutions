# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 왜.. 왜냐고
def find(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                return i, j
    
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(maps, i, j, flag, visit):
    queue = [(i, j, 1)]
    while queue:
        si, sj, cnt = queue.pop(0)
        if maps[si][sj] == flag:
            return si, sj, visit, cnt
        for di, dj in d:
            ni, nj = si+di, sj+dj
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and visit[ni][nj] == 0 and maps[ni][nj] != "X":
                queue.append((ni, nj, cnt+1))
                visit[ni][nj] = cnt
    return -1
    

def solution(maps):
    answer = -2
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    i, j = find(maps)
    findL = bfs(maps, i, j, "L", visit)
    if findL == -1: return -1
    else: i, j, visit, cnt = findL
    answer += cnt
    findE = bfs(maps, i, j, "E", visit)
    if findE == -1: return -1
    else: i, j, visit, cnt = findE
    answer += cnt
    return answer

# 12/1 정해코드
# visit을 bfs 안쪽으로 넣어주면서 해결
def find(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                return i, j
    
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(maps, i, j, flag):
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    queue = [(i, j, 1)]
    while queue:
        si, sj, cnt = queue.pop(0)
        if maps[si][sj] == flag:
            return si, sj, visit, cnt
        for di, dj in d:
            ni, nj = si+di, sj+dj
            if 0 <= ni < len(maps) and 0 <= nj < len(maps[0]) and visit[ni][nj] == 0 and maps[ni][nj] != "X":
                queue.append((ni, nj, cnt+1))
                visit[ni][nj] = cnt
    return -1

def solution(maps):
    answer = -2
    i, j = find(maps)
    for target in ["L", "E"]:
        finds = bfs(maps, i, j, target)
        if finds == -1: return -1
        else: i, j, visit, cnt = finds
        answer += cnt
    return answer
