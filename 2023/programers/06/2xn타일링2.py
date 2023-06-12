# https://www.acmicpc.net/problem/11727 그냥쉬웟더
N = int(input())
dp = [0, 1]
for i in range(1, N+1):
      dp.append(dp[i]+2*dp[i-1])
print(dp[-1]%10007)
