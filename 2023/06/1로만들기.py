# https://www.acmicpc.net/problem/1463

N = int(input())
dp = [0 for _ in range(N+1)]
for i in range(2, N+1):
    if i%3 == 0 and i%2 == 0:
        dp[i] = min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1)
    elif i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i-1]+1)
    elif i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i-1]+1)
    else:
        dp[i] = dp[i-1]+1

print(dp[-1])
