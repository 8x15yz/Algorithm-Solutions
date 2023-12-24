N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[float('inf')]*M for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = [(0, 0, 1)]

while queue:
    si, sj, cnt = queue.pop(0)
    if si == N-1 and sj == M-1:
        print(cnt)
        break
    if dist[si][sj] > cnt:
        dist[si][sj] = cnt
        for di, dj in d:
            if 0 <= si+di < N and 0 <= sj+dj < M \
                    and arr[si+di][sj+dj] == 1 \
                    and dist[si+di][sj+dj] > cnt+1:
                queue.append((si+di, sj+dj, cnt+1))