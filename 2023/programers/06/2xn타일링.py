# https://www.acmicpc.net/problem/11726

N = int(input())
dp = [0, 1]
for i in range(1, N+1):
  dp.append(dp[i-1]+dp[i])

print(dp[-1]%100007)
