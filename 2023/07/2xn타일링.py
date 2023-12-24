# 날먹이라는거임 이게바로 https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    dp = [0, 1]
    for i in range(1, n+1):
        dp += [(dp[i-1]+dp[i])%1000000007]
    return dp[-1]
