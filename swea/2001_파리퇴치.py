# import sys
# sys.stdin = open('2001ans.txt', 'r')

def pari(i, j):
    pariSum = 0
    for verti in range(M):
        for hori in range(M):
            pariSum += arr[i+verti][j+hori]
    return pariSum

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            pariSum = pari(i, j)
            if pariSum > sum:
                sum = pariSum

    print('#{} {}'.format(tc, sum))
