# https://school.programmers.co.kr/learn/courses/30/lessons/12902
# 풀고잇은데 .. 시간초과 정말 때리고싶다

block = {1:3, 2:2}
route = {"A":3, "B":2}
def solution(n):
    # n = 8
    dp = [[], [3], [9, 2]]

    for i in range(3, n//2+1):
        case = []
        for j in range(1, 3):
            mc = ""
            for smc in dp[i-j]:
                mc = smc*block[j]
                case.append(mc)
        dp.append(case)
        
    return sum(dp[-1])%1000000007
