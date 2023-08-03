#https://www.acmicpc.net/problem/15988

dp = [0, 1, 2, 4]
for i in range(int(1e6)):
    dp.append((dp[-1]+dp[-2]+dp[-3])%int(1e9+9))
tc = int(input())
for i in range(tc):
    ans = int(input())
    print(dp[ans])
