def bfs():
    queue = [V]
    visited = []
    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.append(v)
            for node in sorted(tree[v]):
                if node not in visited:
                    queue.append(node)
    return visited

def dfs():
    stack = [V]
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for node in sorted(tree[v], reverse=True):
                if node not in visited:
                    stack.append(node)
    return visited

N, M, V = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

print(*dfs())
print(*bfs())