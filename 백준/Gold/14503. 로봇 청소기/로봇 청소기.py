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
# 1. 현재 위치한 장소를 3으로 변경 (방문처리하기)
    if arr[si][sj] == 0:
        cnt += 1
        arr[si][sj] = 3

# 2. for _ in range(4):
    for _ in range(4):
        rotate(3)
        di, dj = d[0]
        ni, nj = si+di, sj+dj
#       if *(바라보는 곳 기준 왼쪽)으로 공간이있다면 => 왼쪽으로 이동 후 break
        if arr[ni][nj] == 0:
            si, sj = ni, nj
            break
#    else:
    else:
#       if 바라보는 방향 기준 뒤쪽이 벽이라면 => 전체로직 종료 (endFlag 변경)
        di, dj = d[2]
        ni, nj = si+di, sj+dj
        if arr[ni][nj] == 1:
            endFlag = False
#       else => 한칸 후진
        else:
            si, sj = ni, nj

print(cnt)