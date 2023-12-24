#https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    dp = [0, 1, 1]
    cnt = 2
    while cnt < n:
        dp.append(dp[cnt]+dp[cnt-1])
        cnt += 1
    answer = dp[-1]%1234567
    return answer
