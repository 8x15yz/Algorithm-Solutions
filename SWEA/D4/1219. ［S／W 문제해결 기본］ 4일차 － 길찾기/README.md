# [D4] [S/W 문제해결 기본] 4일차 - 길찾기 - 1219 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD) 

### 성능 요약

메모리: 61,952 KB, 시간: 166 ms, 코드길이: 586 Bytes



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do


### 풀이 해설

0에서 시작, dfs 사용해서 node 완전탐색하고 
visited에 99가 있는지를 생각하면 됨
1. answerFlag를 활용 => 99에 방문하면 사실 이후의 탐색들은 필요없기 때문에 가지치기 
2. 그게 아니면 계속 이어진 노드들을 stack에 넣고 dfs를 돌리기
