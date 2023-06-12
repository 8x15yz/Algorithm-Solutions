# https://www.acmicpc.net/problem/9095
# 피보나치 뇌절

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0, 1, 2, 4]
    if N <= 3: 
        print(dp[N])
    else:
        for i in range(4, N+1):
            num = 0
            for j in range(1, 4):
                num += dp[i-j]
            else: dp.append(num)
        print(dp[-1])
