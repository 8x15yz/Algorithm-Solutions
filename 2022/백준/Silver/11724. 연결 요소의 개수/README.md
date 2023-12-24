# [Silver II] 연결 요소의 개수 - 11724 

[문제 링크](https://www.acmicpc.net/problem/11724) 

### 성능 요약

메모리: 182192 KB, 시간: 904 ms

### 분류

그래프 이론(graphs), 그래프 탐색(graph_traversal), 너비 우선 탐색(bfs), 깊이 우선 탐색(dfs)

### 문제 설명

<p>방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.</p>

### 출력 

 <p>첫째 줄에 연결 요소의 개수를 출력한다.</p>
 
### 풀이 
<p> tip => pypy3으로 돌렸음 !!! + 입력받았던 값 N까지 노드가 모두 있다는 점 유의해야됨</p>


<p> 1.1. tree에서 방문하지 않은 node를 찾으면 찾는 즉시 queue에 넣기 </p>
<p> 1.2. for-else문 => 만약에 tree를 다 돌았다는건 일단 묶음들은 다 찾았다는 얘기니까, tree를 한번 더 확인해서 연결 안 된 단일노드들 조사해서 cnt 1씩 누적하기 </p>
<p> 2. bfs 돌려서 queue 마중 노드와 연결된 노드를 찾고 queue비워질때까지 while 돌리기 </p>

![img](https://user-images.githubusercontent.com/87743473/172801623-6a45ffd9-3132-446a-829f-b2f77136b69b.png)
코드 구조화 

