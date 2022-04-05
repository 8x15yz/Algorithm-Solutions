# 1. 1. 그래프 표현 - 인접행렬

`0405 updated!`

```
1. 존재하는 노드 중 최대 노드 크기 만큼의 2차원 배열을 생성 (N*N) 
2. 각 노드가 이어져있으면 1표시, else 0표시 => i에서 j로 가는 경로가 있으면 adj[i][j] = 1
3. 무향의 경우: 경로가 서로 있는거라 봐도 무방함
ex)
       (0)   (0 -> 1)       | 0 | 1 | 1 |   adj[0][1] = 1
     >/   \>  (0 -> 2)		| 0 | 0 | 0 |   adj[0][2] = 1
   (2)  -> (1)  (2 -> 1)	| 0 | 1 | 0 |   adj[2][1] = 1
```





# 1.2. 그래프 표현 - 인접 리스트

`0405 updated!`

```
1. 역시 존재하는 노드 중 최대 노드 크기만큼의 배열을 생성(N)
2. 노드에 해당하는 인덱스의 배열에 해당 노드와 이어진 노드들의 정보를 모두 기재
ex) 위 예시의 경우 => adj = [[1, 2], [], [1]]
```





# 2. disjoint sets

`0405 updated!`

```
1. 상호배타 집합이란? => 서로 교집합을 가지고 있지 않은 집합들이며
2. 두 집합은 각 대표원소로 구분을 함
3. disjoint sets를 표현하는 방법은 트리(연결리스트)가 있음
   => 연산 3가지 makeset/ findset/ union
```

```
1. makeset) 모든 노드들에 대해 개별집합을 만들어주는 작업
   parents = [x for x in range(N)]
   
2. findset) input값 x를 포함하는 집합을 찾는 작업인데
   findset(x):
	 if x == parents[x] : return x
	 else 				: return findset(x)
	 
   반복문으로도 만들수있음	 
   findset(x):
   	 while x != parent[x]
   	 	x = parent[x]
   	 return x
	 
3. union) x, y를 포함하는 두 집합을 통합하는 작업
   union(x, y):
   	 p[findset(y)] = findset(x)
```





# 3.1. MST (Minimum Spanning Tree)

최소비용 신장트리 `0405 updated!`

```
"모든 노드가 연결되어있는 트리인데 그 간선들의 가중치 합이 최소가 되는"

신장트리 개념 자체가 
"간선을 최소로 하여 모든 노드를 연결한 무방향 + 사이클없는 그래프" 
여기서 최소비용이 붙으면 => 가중치가 붙고 "무방향 + 가중치 있는"
```

MST를 만드는 알고리즘 두가지 => 크루스칼 알고리즘 + 프림 알고리즘



# 3.2. 크루스칼 알고리즘

`0405 updated!`

간선삭제+간선삽입 두가지 방법이있는데 내가배운건 "간선삽입"

크루스칼알고리즘이 disjoint sets를 활용하고 잇음 

```
1. 가중치 오름차순 정렬
2. 모든 노드에 대해 makeset
3. 최초 mst는 공집합으로 설정
4. 노드 수-1 만큼 다음을 반복함:
	최소 가중치를 가진 간선부터 조회하면서 간선이 잇고있는 두개의 노드에 대해 현재
	사이클을 생성하지 않고있는지 (즉 서로 다른 집합의 원소인지를 알아야됨)를 파악
5. 4를 검증했을때 서로 다른 집합의 노드임이 확인되면 mst에 간선의 노드정보를 추가하고 비용을 누적함
```



##### cf) swea 5249 크루스칼으로 풀이하였음

```python
# 크루스칼 알고리즘을 사용하여 풀이함
def findset(x):
    if x == p[x]:
        return x
    else:
        return findset(p[x])            # 인덱스와 값이 동일하다면 => 본인을 가리키고 있는거니까 대표노드

def union(x, y):
    p[findset(y)] = findset(x)          # 유니온 작업을 할 때 대표노드를 끌고와야되니까 findset 해서 제일 부모노드를 찾아줌

import sys
sys.stdin = open('5249.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        nodes.append((w, n1, n2))
    nodes = sorted(nodes)               # 가중치가 가장 낮은 간선부터 선택하기 위함

    p = [i for i in range(1001)]        # makeset
    mst = []                            # 최초 mst는 공집합으로 설정
    mst_cost = 0                        # mst가중치를 누적할 변수

    while len(mst) < V:                 # 정점의 수-1 만큼 반복
        val, u, v = nodes.pop(0)        # 최소 가중치를 가진 간선 가져오기
        if findset(u) != findset(v):    # 노드 n1, n2 가 서로 다른 집합의 원소인지를 확인해야됨
            union(u, v)                 # => 같은집합이면 사이클 생기니까 안돼
            mst.append((u, v))
            mst_cost += val

    print('#{} {}'.format(tc, mst_cost))
```

