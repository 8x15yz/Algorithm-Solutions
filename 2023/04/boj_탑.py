# https://www.acmicpc.net/problem/2493

## 시간초과 .......
N = int(input())
tops = [10*9] + list(map(int, input().split()))
answer = []

for t in range(1, len(tops)):
  for i in range(t-1, -1, -1):
    if tops[t] < tops[i]:
      answer.append(i)
      break
print(*answer)

