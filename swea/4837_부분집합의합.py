# import sys
# sys.stdin = open('4837ans.txt', 'r')

def combination(p, r, n):
    global cnt
    if n == N and sum(p) == K:
        cnt += 1
        return
    if len(p) == 0:
        smallest = 1
    else:
        smallest = p[-1]
    for i in range(smallest, r):
        if not i in p:
            p.append(i)
            combination(p, r, n+1)
            p.pop()

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0
    combination([], 13, 0)

    print('#{} {}'.format(tc, cnt))
