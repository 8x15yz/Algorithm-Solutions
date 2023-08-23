# https://level.goorm.io/exam/195690/통증/
## 진짜 난 바보야 ...
## 정답
N = int(input())
answer = 0
for item in [14, 7, 1]:
	answer += N//item
	N %= item

print(answer)


## 호출에러난거 dfs 재귀
def dfs(N, cnt):
	global answer
	if cnt > answer: return
	if n == 0:
		answer = cnt
		return
	for item in [N-14, N-7, N-1]:
		if item < 0: continue
		dfs(item, cnt + 1)


global answer
N = int(input())
answer = 1e9
dfs(N, 0)
print(answer)


## 시간초과에러난거 bfs
N = int(input())
def bfs(N, cnt):
	queue = [(N, cnt)]
	visit = []
	
	while queue:
		N, cnt = queue.pop(0)
		if N == 0: return cnt
		for op in [N-1, N-7, N-14]:
			if 0 <= op <= 10e9 and op not in visit:
				queue.append((op, cnt+1))
				visit.append(op)
				
	else: return -1

print(bfs(N, 0))

