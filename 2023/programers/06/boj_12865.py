# https://www.acmicpc.net/problem/12865
N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for n in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        dp[n][j] = max(V + dp[n-1][j-W], dp[n-1][j]) if W <= j else dp[n-1][j]
        
print(dp[N][K])
