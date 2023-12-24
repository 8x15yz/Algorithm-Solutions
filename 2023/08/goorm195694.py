#https://level.goorm.io/exam/195694/발전기/

## 오늘 느낀점 : 방문처리배열 하나가 열개 추가기능보다 낫다 ~~!!

## 통과한 귀염깔끔코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dt = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visit = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
for i in range(N):
	for j in range(N):
		if arr[i][j] == 1 and not visit[i][j]:
			visit[i][j] = 1
			queue = [(i, j)]
			while queue:
				si, sj = queue.pop(0)
				for di, dj in dt:
					if 0 <= (ni := di+si) < N and 0 <= (nj := dj+sj) < N and not visit[ni][nj] and arr[ni][nj] == 1:
							queue.append((ni, nj))
							visit[ni][nj] = 1		
			else: cnt += 1
		
print(cnt)



##시간초과 피하려고 여러가지 떡칠했지만 통과못한코드
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dt = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visit = []
cnt = 0
for i in range(N):
	for j in range(N):
		if arr[i][j] == 1 and (i, j) not in visit:
			visit += [(i, j)]
			queue = deque([(i, j)])
			while queue:
				si, sj = queue.popleft()
				for di, dj in dt:
					if 0 <= (ni := di+si) < N and 0 <= (nj := dj+sj) < N and arr[ni][nj] == 1 and (ni, nj) not in visit:
							queue += [(ni, nj)]
							visit += [(ni, nj)]			
			else: cnt += 1
		
print(cnt)



