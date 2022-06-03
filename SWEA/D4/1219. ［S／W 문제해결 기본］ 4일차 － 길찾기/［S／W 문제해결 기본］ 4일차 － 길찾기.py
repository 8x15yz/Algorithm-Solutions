# import sys
# sys.stdin = open('1219ans.txt', 'r')


for _ in range(1, 11):
    tc, N = map(int, input().split())
    datum = list(map(int, input().split()))
    graph = [[] for _ in range(100)]

    for n in range(N):
        graph[datum[n*2]].append(datum[n*2+1])

    answerFlag = 0
    stack = [0]
    visited = []

    while stack:
        v = stack.pop()
        visited.append(v)
        if v == 99:
            answerFlag = 1
            break
        if graph[v]:
            for node in graph[v]:
                stack.append(node)

    print('#{} {}'.format(tc, answerFlag))
