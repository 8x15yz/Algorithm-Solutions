https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc

# 브루트포스 돌리려했더니 시간초과남
T = int(input())
for tc in range(1, T+1):
  N, M, K = map(int, input().split())
  pList = list(map(int, input().split()))
  wList, bList = [0]*(sum(pList)+1), [0]*(sum(pList)+1)
  a = 1
  runTime = len(wList)
  for i in range(runTime):
    if i == sum(pList[:a]):
      wList[i] += 1
      a += 1
    if i%(M+1) == M:
      bList[i] += K

  charge = 0
  for i in range(runTime):
    charge += bList[i]
    charge -= wList[i]
    if charge == -1:
      print('#{} Impossible'.format(tc))
      break
  else:
    print('#{} Possible'.format(tc))
