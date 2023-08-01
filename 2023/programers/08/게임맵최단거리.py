# https://school.programmers.co.kr/learn/courses/30/lessons/1844
dt = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def solution(maps):
    N, M = len(maps), len(maps[0])
    visit = []
    for i in range(N):
        for j in range(M):
            if maps[i][i] and (i, j) not in visit:
                stack = [(i, j, 0)]
                while stack:
                    si, sj, route = stack.pop()
                    print(si, sj, route)
                    visit.append((si, sj))
                    for di, dj in dt:
                        if 0 <= si+di < N and 0 <= sj+dj < M and (si+di, sj+dj) not in visit:
                            if (si+di, sj+dj) == (N-1, M-1): 
                                return route
                            elif maps[si+di][sj+dj]:
                                stack.append((si+di, sj+dj, route+1))
                                
    return answer 


# 아오 ~~~~~ 아직 푸는중
dt = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(maps):
    N, M = len(maps), len(maps[0])
    visit = [(0, 0)]
    for i in range(N):
        for j in range(M):
            if maps[i][j]:
                visit.append((i, j))
                queue = [(i, j, 1)]
                while queue:
                    # print(queue)
                    si, sj, route = queue.pop(0)
                    # print(si, sj, route)
                    if si == N-1 and sj == M-1: return route
                    else:
                        for di, dj in dt:
                            ni, nj = si+di, sj+dj
                            if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] and (ni, nj) not in visit:
                                # print(maps[ni][nj], maps[si][sj], si, sj, ni, nj)
                                visit.append((ni, nj))
                                queue.append((ni, nj, route+1))

