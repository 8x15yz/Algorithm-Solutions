# https://school.programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    answer = 0
    # 같은 열 연속 불가
    L = len(land)
    dp = [0 for _ in range(L)]
    checkL = -1
    for i in range(L):
        maxL = -1
        for j in range(4):
            if maxL < land[i][j] and j != checkL: 
                maxL = land[i][j]
                fCheck = j
        else: 
            checkL = fCheck
            dp[i] = maxL if i == 0 else dp[i-1] + maxL
    
    return dp[-1]
