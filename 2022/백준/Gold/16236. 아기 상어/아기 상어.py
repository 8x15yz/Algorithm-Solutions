# import sys
# sys.stdin = open('16236ans.txt', 'r')

d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
levelnCnt = [2, 1]

# 상어 위치 찾기 + 초기화
si, sj = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[i][j] = 0

#
while True:
    queue = [(si, sj, 0)]
    varr = [[] for _ in range(1000)]
    visited = []

    while queue:
        si, sj, cnt = queue.pop(0)
        visited.append((si, sj))
        if 0 < arr[si][sj] < levelnCnt[0]:
            varr[cnt].append((si, sj))
        for di, dj in d:
            ni, nj = si+di, sj+dj
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and arr[ni][nj] <= levelnCnt[0]:
                queue.append((ni, nj, cnt + 1))
                visited.append((ni, nj))
    # print(levelnCnt, varr)
    for i in range(1000):
        if varr[i]:
            si, sj = sorted(varr[i])[0]
            arr[si][sj] = 0
            ans += i
            if levelnCnt[1] == levelnCnt[0]:
                levelnCnt[0] += 1
                levelnCnt[1] = 1
            else:
                levelnCnt[1] += 1
            break
    else:
        print(ans)
        break