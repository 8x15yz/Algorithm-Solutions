# import sys
import itertools
# sys.stdin = open('boj_15686.txt', 'r')

def calcway(case):
    ssum = 0
    for hi, hj in house:
        track = []
        for c in case:
            ci, cj = c
            dist = abs(hi-ci)+abs(hj-cj)
            track.append(dist)
        ssum += min(track)
    return ssum

# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 지도 내에서 2의 갯수를 세고
m = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            m.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))
# print(house)
C = len(m)
ans = []
if M == 1:       # 하나만 남겨야 되는 경우 => 모든 케이스에 대해 각각의 값을 계산하고 그중 최소를 출력하기
    for case in m:
        a = calcway([case])
        ans.append(a)

elif C == M:     # 2의 갯수와 남겨야되는 갯수가 동일한경우 => 한번의 케이스에 대해만 게산하면 됨
    a = calcway(m)
    ans.append(a)
else:            # 몇개를 빼야되는 경우
    for cases in itertools.combinations([x for x in range(C)], M):
        case = []
        for c in cases:
            case.append(m[c])
        a = calcway(case)
        ans.append(a)
print(min(ans))