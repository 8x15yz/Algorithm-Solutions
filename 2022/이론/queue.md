# 1. 큐 구현하기

## 1.1. 선형큐

```python 
a = [1, 2, 3]

queue = []
front = 0
rear = 0
# 큐 삽입 과정
while rear != len(a):
    queue.append(a[rear])
    rear += 1
    print(queue)
# 큐 삭제과정
while front != len(a):
    queue.pop(0)
    front += 1
    print(queue)
```



## 1.2. 원형큐







# 2. BFS

## 2.1. swea 5102 노드의거리

`0317 updated!`

```python
#import sys
#sys.stdin = open('5102.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    tree = []
    dist = [0]*51
    for i in range(51):
        tree.append([])

    for e in range(E):
        e1, e2 = map(int, input().split())
        tree[e1].append(e2)               # 방향이 없으므로 양쪽 노드 모두 시작점이 될 수 있음
        tree[e2].append(e1)
    S, G = map(int, input().split())

    queue = [S]                           # BFS 사용 : 미리 큐에 시작노드 넣어놓기
    visit = []

    while queue:                          # 큐가 비어있게 될 때 까지
        v = queue.pop(0)                  # 큐에서 빼서 조회하고
        visit.append(v)                   # 방문처리
        for node in tree[v]:              # 조회하는 노드의 하위노드들에 대해
            if node not in visit:         # 방문 안 한 노드만
                queue.append(node)        # 큐에 넣고
                visit.append(node)        # 방문처리한번더 ** 이부분이 중요 !!
                dist[node] = dist[v] + 1  # 조회하는 노드의 거리는 상위노드 거리 + 1

    print('#{} {}'.format(tc, dist[G]))   # G까지의 거리를 출력하고 
                                          # 노드가 이어져있지 않으면 자연스레 0 을 촐력하게됨
```



## 2.2. swea 5105 노드의거리

0325 풀이완

```python 
def bfs(I, J):
    queue = [(I, J)]
    visit = []

    while queue:
        vi, vj = queue.pop(0)
        if arr[vi][vj] == '3':
            # print('도착 !!', vi, vj)
            return

        elif (vi, vj) not in visit:
            visit.append((vi, vj))

            for di, dj in d:
                if 0<=vi+di<N and 0<=vj+dj<N:
                    if arr[vi+di][vj+dj] == '0':
                        queue.append((vi+di, vj+dj))
                        way[vi+di][vj+dj] += way[vi][vj] +1
                    elif arr[vi+di][vj+dj] == '3':
                        queue.append((vi + di, vj + dj))
    # else:
    #     # print('길이없어 ..')


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    way = [[0]*N for _ in range(N)]

    # for i in range(N):
    #     print(arr[i])

    for i in range(N):
        if '2' in arr[i]:
            si, sj = i, arr[i].index('2')
        elif '3' in arr[i]:
            ei, ej =i,  arr[i].index('3')

    bfs(si, sj)

    # for i in way:
    #     print(i)
    ans = []
    for ai, aj in d:
        if 0 <= ei + ai < N and 0 <= ej + aj < N:
            if way[ei + ai][ej + aj] != 0:
                ans.append(way[ei + ai][ej + aj])
    if ans == []:
        answer = 0
    else:
        answer = min(ans)

    print('#{} {}'.format(tc, answer))
```

