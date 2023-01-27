# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 틀린코드 다시 풀어봐야됨
def solution(N, stages):
    answer = []
    stgUsers = [0 for _ in range(N+1)]
    for user in stages:
        if user > N:
            stgUsers[0] += 1
        else:
            stgUsers[user] += 1
            
            
    player = len(stages)
    failper = [0 for _ in range(N)]
    for i in range(1, len(stgUsers)):
        if stgUsers[i] != 0:
            failper[i-1] = stgUsers[i]/player
        player -= stgUsers[i]
    
    visited = [0 for _ in range(N)]
    while sum(visited) < N:
        for i in range(N):
            if failper[i] == max(failper) and visited[i] == 0:
                answer.append(i+1)
                failper[i] = 0
                visited[i] = 1
        
    return answer
