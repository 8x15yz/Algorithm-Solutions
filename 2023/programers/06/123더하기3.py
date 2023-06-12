#https://www.acmicpc.net/problem/15988


# 나를 추잡하게 만드는 문제 ...
# 자료구조를 바꿔봐야될 것 같다
from collections import deque
import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    dp = deque([0, 1, 2, 4])
    if N <= 3: print(dp[N]%1000000009)
    else:
        for _ in range(4, N+1):
            num = 0
            for j in range(1, 4):
                num += dp[4-j]
            else: 
              dp += [num]
              dp.popleft() 
        print(dp[-1]%1000000009)
