# https://level.goorm.io/exam/88520/놀이공원

for tc in range(int(input())):
	N, K = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(N)]
	
	minwst = 999999
	for i in range(N-K+1):
		for j in range(N-K+1):
			waste = 0
			for k in range(i, i+K):
				for l in range(j, j+K):
					if arr[k][l] == 1: waste += 1
			else:
				if minwst > waste: minwst = waste
	print(minwst)
