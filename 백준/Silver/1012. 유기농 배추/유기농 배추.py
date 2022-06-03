import sys
from collections import deque

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    queue = deque()
    queue.append((i, j))

    while queue:
        si, sj = queue.popleft()
        arr[si][sj] = 0
        for di, dj in d:
            ni, nj = di+si, dj+sj
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 1:
                arr[ni][nj] = 0  # Key Code!! 중복방문되지 않게 방문처리해주는 코드 추가
                queue.append((ni, nj))

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    M, N, K = map(int,sys.stdin.readline().split())
    arr = [[0]*N for _ in range(M)]
    
    for _ in range(K):
        i, j = map(int,sys.stdin.readline().split())
        arr[i][j] = 1

    cnt = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                bfs()
    print(cnt)
