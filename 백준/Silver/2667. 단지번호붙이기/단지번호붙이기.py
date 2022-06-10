N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

visited = []
cntList = []


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and (i, j) not in visited:
            cnt = 0
            queue = [(i, j)]
            while queue:
                vi, vj = queue.pop(0)
                visited.append((vi, vj))
                cnt += 1
                for di, dj in d:
                    ni, nj = vi + di, vj + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and (ni, nj) not in visited:
                        queue.append((ni, nj))
                        visited.append((ni, nj))
            cntList.append(cnt)
print(len(cntList))
for cnt in sorted(cntList):
    print(cnt)
