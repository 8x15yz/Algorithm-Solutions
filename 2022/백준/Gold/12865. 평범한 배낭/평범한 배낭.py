import sys
N, K = map(int, sys.stdin.readline().strip().split())
value = [[0]*N for _ in range(2)]
dpArray = [[0]*(K+1) for _ in range(N+1)]
for i in range(N):
    value[0][i], value[1][i] = map(int, sys.stdin.readline().strip().split())

for n in range(1, N+1):
    for w in range(1, K+1):
        if value[0][n-1] <= w:
            dpArray[n][w] = max(value[1][n-1] + dpArray[n-1][w-value[0][n-1]], dpArray[n-1][w])
        else:
            dpArray[n][w] = dpArray[n-1][w]

print(dpArray[N][K])
