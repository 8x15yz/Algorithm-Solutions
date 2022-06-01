# import sys
# sys.stdin = open('1210ans.txt', 'r')

d = [(-1, 0), (0, -1), (0, 1)]

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    si, sj = 99, arr[99].index(2)

    while si > 0:
        for di, dj in d:
            if 0 <= si + di <= 99 and 0 <= sj + dj <= 99 and arr[si + di][sj + dj] == 1:
                arr[si][sj] = 0
                si, sj = si+di, sj+dj

    print('#{} {}'.format(tc, sj))