# dp 문제 
N = int(input())
ans = 0
def calcul(n):
  global ans
  if n == 1:
    return 1
  elif n%2 == 0:
    ans += 1
    return calcul(n//2)
  elif (n-3)%6 == 0:
    ans += 1
    return calcul(n//3)
  else:
    ans += 1
    return calcul(n-1)

calcul(N)
print(ans-1)


#이게 아니래 ..

import math

N = int(input())
ans = 0


def calcul(n):
    global ans
    if n == 1:
        return ans
    elif math.sqrt(n-1) == int(math.sqrt(n-1)):
        ans += 1
        return calcul(n - 1)
    elif n % 2 == 0:
        ans += 1
        return calcul(n // 2)
    elif (n - 1) % 6 == 0:
        ans += 1
        return calcul(n - 1)
    elif (n + 3) % 6 == 0:
        ans += 1
        return calcul(n // 3)


print(calcul(N))


# tq


# 정답코드
# 재귀가 아니라 이게 맞다니 정말 분하다
N = int(input())

dp = [0, 0, 1, 1]
for i in range(4, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        dp.append(min(dp[i // 2] + 1, dp[i // 3] + 1, dp[i - 1] + 1))
    elif i % 2 == 0 and i % 3 != 0:
        dp.append(min(dp[i // 2] + 1, dp[i - 1] + 1))
    elif i % 2 != 0 and i % 3 == 0:
        dp.append(min(dp[i // 3] + 1, dp[i - 1] + 1))
    else:
        dp.append(dp[i - 1] + 1)
if N == 1:
    print(0)
else:
    print(dp[-1])
