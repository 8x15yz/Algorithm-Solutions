# import sys
# sys.stdin = open('1226ans.txt', 'r')

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    si, sj, answer = 0, 0, 0
    endFlag = 0
    while endFlag == 0:
        for i in range(16):
            for j in range(16):
                if arr[i][j] == 2:
                    si, sj = i, j
                    endFlag = 1

    visited = []
    stack = [(si, sj)]

    while stack:
        vi, vj = stack.pop()
        visited.append((vi, vj))
        if arr[vi][vj] == 3:
            answer = 1
            break
        for di, dj in d:
            ni, nj = vi+di, vj+dj
            if 0 <= ni <= 15 and 0 <= nj <= 15 \
            and (ni, nj) not in visited \
            and arr[ni][nj] != 1:
                stack.append((ni, nj))

    print('#{} {}'.format(tc, answer))
