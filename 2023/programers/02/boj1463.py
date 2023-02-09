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
