# https://level.goorm.io/exam/195688/문자열-나누기
from itertools import combinations
N = int(input())
S = list(input())
reward = []
compare = []
for i, j in list(combinations([i for i in range(1, N)], 2)):
	toTuple = []
	for f, b in [(0, i), (i, j), (j, N)]:	
		if "".join(S[f:b]) not in reward: reward.append("".join(S[f:b]))
		toTuple.append("".join(S[f:b]))
	else: 
		compare.append(tuple(toTuple))
rewardict = {}
reward = sorted(reward)
for r in range(len(sorted(reward))):
	rewardict[reward[r]] = r+1

maxnum = 0
for a, b, c in compare:
	if rewardict[a]+rewardict[b]+rewardict[c] > maxnum:
		maxnum = rewardict[a]+rewardict[b]+rewardict[c]
print(maxnum)
	
