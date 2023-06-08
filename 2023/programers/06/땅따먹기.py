# https://school.programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    answer = 0
    # 같은 열 연속 불rk
    L = len(land)
    for c in range(4):
        dp = [0 for _ in range(L)]
        checkL = c
        dp[0] = land[0][c]
        for i in range(1, L):
            maxL = -1
            for j in range(4):
                if maxL < land[i][j] and j != checkL: 
                    maxL = land[i][j]
                    fCheck = j
            else: 
                checkL = fCheck
                dp[i] = dp[i-1] + maxL
        else:
            answer = dp[-1] if answer < dp[-1] else answer
    
    return answer
