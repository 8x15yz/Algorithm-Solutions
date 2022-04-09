# import sys
import itertools
# sys.stdin = open('boj_14502.txt', 'r')
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def expend(si, sj):
    queue = [(si, sj)]
    visit = []
    while queue:
        v = queue.pop(0)
        if v not in visit:
            visit.append(v)
            vi, vj = v
            for di, dj in d:
                if 0 <= vi+di <N and 0<=vj+dj <M and tarr[vi+di][vj+dj] == 0:
                    tarr[vi + di][vj + dj] = 2
                    queue.append((vi+di, vj+dj))
    return


# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

candi = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            candi.append((i, j))

C = len(candi)
ans = []
for case in itertools.combinations([x for x in range(C)], 3):
    # brute force 위한 임시리스트 만들기
    tarr = []
    for i in range(N):
        track = []
        for j in range(M):
            track.append(arr[i][j])
        tarr.append(track)

    # 임시 리스트에서 3개 벽 후보를 정하여 1 적용해주는 모습
    for xy in case:
        x, y = candi[xy]
        tarr[x][y] = 1

    # 벽을 다 쳐놓은 상태에서 바이러스 확산을 구현하기
    for i in range(N):
        for j in range(M):
            if tarr[i][j] == 2:
                expend(i, j)


    # 바이러스 확산 후 0의 갯수를 세기
    ansd = 0
    for i in range(N):
        ansd += tarr[i].count(0)
    # for a in range(N):
    #     print(tarr[a])
    # print(ansd)


    ans.append(ansd)
print(max(ans))