# https://www.acmicpc.net/problem/12886
# 이런 허벌문제가 골드 5라니 ..
# 연산순서 '*', '+', '-', '/'

s, t = map(int, input().split())

def bfs(s, cnt):
    if s == t: return 0
    visit = []
    limit = 10e9
    queue = [(s, "")]
    cnt = 0

    while queue:
        i, hist = queue.pop(0)
        if i == t: return hist
        for op, cal in [(i*i, "*"), (i+i, "+"), (1, "/")]:
            if op <= limit and op not in visit: 
                queue.append((op, hist+cal))
                visit.append(op)
            
    else: return -1
        

print(bfs(s, 0))
