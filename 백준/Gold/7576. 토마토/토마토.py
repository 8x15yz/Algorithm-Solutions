from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
varr = [[0]*M for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

lastCnt= 0
si, sj = 0, 0

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            si, sj = i, j
            queue.append((si, sj, 0))
            varr[si][sj] = 1
while queue:
    si, sj, cnt = queue.popleft()
    arr[si][sj] = 1
    lastCnt = cnt
    for di, dj in d:
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and not varr[ni][nj]:
            queue.append((ni, nj, cnt + 1))
            varr[ni][nj] = 1

for t in arr:
    if 0 in t:
        lastCnt = -1

print(lastCnt)