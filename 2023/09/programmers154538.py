# https://school.programmers.co.kr/learn/courses/30/lessons/154538


# bfs 쓰고 "하향식"으로 풀이함
# 하향식으로 풀이하면 (원하는답에서 인풋값을 내는 방향) 나누기할 때 나오는 float 형식 값들을 가지치기 할 수 있기 때문에 시간단축 됨
def solution(y, x, n):
    queue = [(x, 0)]
    visit = [0 for _ in range(int(10e6)+1)]
    
    while queue:
        x, query = queue.pop(0)
        if x == y: return query
    
        if 0 <= x-n <= 10e6 and not visit[x-n]:
            queue.append((x-n, query+1))
            visit[x-n] = 1
        for i in (2, 3):
            if x%i == 0 and 0 <= (case := x//i) <= 10e6 and not visit[case]:
                queue.append((case, query+1))
                visit[case] = 1
    return -1
