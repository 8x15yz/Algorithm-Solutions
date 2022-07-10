N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

pow = {'W' : 0, 'B' : 0}
mainColor = 'A'
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            si, sj = i, j
            visited[si][sj] = 1
            mainColor = arr[si][sj]
            queue = [(si, sj)]
            cnt = 0
            mainColor = arr[si][sj]
            while queue:
                vi, vj = queue.pop(0)
                cnt += 1
                for di, dj in d:
                    ni, nj = vi+di, vj+dj
                    if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] == mainColor:
                        queue.append((ni, nj))
                        visited[ni][nj] = 1
            pow[mainColor] += cnt**2
print(pow['W'], pow['B'])
