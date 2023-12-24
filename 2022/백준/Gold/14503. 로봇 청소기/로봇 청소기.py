# *바라보는 곳 기준 왼쪽 idx
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def rotate(n):
    for _ in range(n):
        dPop = d.pop(0)
        d.append(dPop)

N, M = map(int, input().split())
r, c, dv = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

rotate(dv)
si, sj, cnt, endFlag = r, c, 0, True

while endFlag:
    if arr[si][sj] == 0:
        cnt += 1
        arr[si][sj] = 3

    for _ in range(4):
        rotate(3)
        di, dj = d[0]
        ni, nj = si+di, sj+dj
        if arr[ni][nj] == 0:
            si, sj = ni, nj
            break
    else:
        di, dj = d[2]
        ni, nj = si+di, sj+dj
        if arr[ni][nj] == 1:
            endFlag = False
        else:
            si, sj = ni, nj

print(cnt)
