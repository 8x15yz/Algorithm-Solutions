# https://level.goorm.io/exam/195692/gamejam/

d = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
N = int(input())
rg, cg = map(int, input().split())
rp, cp = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

def play(vi, vj):
	visit = []
	while (vi, vj) not in visit:
		drct, nxt = arr[vi][vj][-1], int(arr[vi][vj][:-1])
		for _ in range(nxt):
			visit.append((vi, vj))
			ni, nj = (vi+d[drct][0])%N, (vj+d[drct][1])%N
			if (ni, nj) in visit: 
				return len(visit) 
			vi, vj = ni, nj
	return len(visit)

goorm = play(rg-1, cg-1)
player = play(rp-1, cp-1)
if goorm > player: print("goorm", goorm)
else: print("player", player)

