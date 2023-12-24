# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 틀린코드 다시 풀어봐야됨 
# 74.1점
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

[다중리스트 정렬방법](https://shoney.tistory.com/entry/Python-%EB%8B%A4%EC%A4%91-%EB%A6%AC%EC%8A%A4%ED%8A%B8List-%EC%A0%95%EB%A0%AC-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84)
# 다중 리스트 정렬방법으로 풀어봄
# 오답, 70.4점
def solution(N, stages):
    answer = []
    stage = [0 for _ in range(N+1)] # 0:완료, 1~N:잔류
    player = len(stages)
    for mem in stages:
        if mem == N+1:
            stage[0] += 1
        else:
            stage[mem] += 1
            
    failure = [[0, i+1] for i in range(N)]
    for mem in range(1, len(stage)):
        failure[mem-1][0] = stage[mem]/player
        player -= stage[mem]
        
    for ans in sorted(failure, reverse=True, key=lambda x:x[0]):
        answer.append(ans[1])
    
    return answer

## 정답코드 : 제로디비전에러 고려하기
def solution(N, stages):
    answer = []
    stage = [0 for _ in range(N+1)] # 0:완료, 1~N:잔류
    player = len(stages)
    for mem in stages:
        if mem == N+1:
            stage[0] += 1
        else:
            stage[mem] += 1
            
    failure = [[0, i+1] for i in range(N)]
    for mem in range(1, len(stage)):
        if stage[mem] !=0 and stage[mem] !=0: ## 제로디비전에러를 고려하기
            failure[mem-1][0] = stage[mem]/player
        player -= stage[mem]
        
    for ans in sorted(failure, reverse=True, key=lambda x:x[0]):
        answer.append(ans[1])
    
    return answer


## 정답코드 : 제로디비전에러 고려하기 + 람다로 리스트 정렬 꼭 하기
def solution(N, stages):
    answer = []
    stage = [0 for _ in range(N+1)] # 0:완료, 1~N:잔류
    player = len(stages)
    for mem in stages:
        if mem == N+1:
            stage[0] += 1
        else:
            stage[mem] += 1
            
    failure = [[0, i+1] for i in range(N)]
    for mem in range(1, len(stage)):
        if stage[mem] !=0 and stage[mem] !=0: ## 제로디비전에러를 고려하기
            failure[mem-1][0] = stage[mem]/player
        player -= stage[mem]
        
    for ans in sorted(failure, reverse=True, key=lambda x:x[0]):
        answer.append(ans[1])
    
    return answer

