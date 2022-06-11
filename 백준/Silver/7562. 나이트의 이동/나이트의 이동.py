from collections import deque
d = [
    (-2, -1), (-1, -2),
    (2, -1), (1, -2),
    (-2, 1), (-1, 2),
    (2, 1), (1, 2)
     ]

T = int(input())
for _ in range(T):
    N = int(input())
    si, sj = map(int, input().split())
    vi, vj = map(int, input().split())
    cnt = 0
    queue = deque()
    queue.append((si, sj, 0))
    varr = [[0]*N for _ in range(N)]
    while queue:
        si, sj, cnt = queue.popleft()
        if si == vi and sj == vj:
            print(cnt)
            queue = []
            break
        varr[si][sj] = 1
        for di, dj in d:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and not varr[ni][nj]:
                queue.append((ni, nj, cnt+1))
                varr[ni][nj] = 1
                if ni == vi and nj ==vj:
                    print(cnt + 1)
                    queue = []
                    break