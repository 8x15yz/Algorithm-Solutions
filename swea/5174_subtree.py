# import sys
# sys.stdin = open('5174ans.txt', 'r')

def findnode(N):
    global cnt
    if tree[N]:
        for node in tree[N]:
            cnt += 1
            findnode(node)


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]

    for i in range(E):
        tree[data[i*2]].append(data[i*2+1])

    cnt = 1
    findnode(N)
    print('#{} {}'.format(tc, cnt))
