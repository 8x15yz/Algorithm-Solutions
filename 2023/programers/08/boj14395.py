# https://www.acmicpc.net/problem/12886
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
        if (op := i*i) <= limit and op not in visit: 
            queue.append((op, hist+"*"))
            visit.append(op)

        if (op := i+i) <= limit and op not in visit: 
            queue.append((op, hist+"+"))
            visit.append(op)

        if (op := 1) <= limit and op not in visit: 
            queue.append((op, hist+"/"))
            visit.append(op)
            
    else: return -1
        

print(bfs(s, 0))
