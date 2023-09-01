# https://level.goorm.io/exam/195697/과일-구매
N, K = map(int, input().split())
rem = []
for _ in range(N):
	p, c = map(int, input().split())
	rem.append((p, c, c//p))
rem.sort(key = lambda x: x[-1], reverse = True)

def cal(rem):
	w, v = 0, 0
	for p, c, unit in rem:
		if w+p <= K:
			w += p
			v += c
			continue
		for i in range(c):
			if w+1 <= K:
				w += 1
				v += unit
			else: return v
	return v
print(cal(rem))

## 이게 정해코드라고함 ~ 이거 보니까 내 코드 시갖초과 날만하다
def solution(n):
    count = 1
    for j in range(1,n):
        m1 = j
        while True:
            if j == n:
                count += 1
                break
            elif j > n:
                break
            m1 += 1
            j += m1

    return count
