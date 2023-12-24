N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
for n in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

cnt = 0
visited = []

while True:
    queue = []
    for node in range(1, N+1):
        if node not in visited and tree[node]:
            queue.append(node)
            cnt += 1
            break
    else:
        for node in range(1, N+1):
            if node not in visited and not tree[node]:
                cnt += 1
        break

    while queue:
        v = queue.pop()
        for node in tree[v]:
            if node not in visited:
                queue.append(node)
                visited.append(node)

print(cnt)