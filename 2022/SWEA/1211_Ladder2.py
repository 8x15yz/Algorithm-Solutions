# import sys
# sys.stdin = open('1211ans.txt', 'r')

d = [(0, 1), (1, 0), (0, -1)]

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    min, minDex = float('inf'), 0

    for startJ in range(100):
        if arr[0][startJ] == 1:
            cnt, si, sj = 0, 0, startJ
            visited = [(si, sj)]

            while si < 99:
                if min <= cnt:
                    break
                for di, dj in d:
                    if (si+di, sj+dj) not in visited:
                        if 0 <= si+di <= 99 and 0 <= sj+dj <= 99 and arr[si+di][sj+dj] == 1:
                            visited.append((si, sj))
                            si, sj = si+di, sj+dj
                            cnt += 1
            else:
                min = cnt
                minDex = startJ
    print('#{} {}'.format(tc, minDex))
