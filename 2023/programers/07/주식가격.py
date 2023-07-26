# https://school.programmers.co.kr/learn/courses/30/lessons/42584

# 이게문제냐?
def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        z = 1
        for j in range(i+1, len(prices)-1):
            if prices[i] > prices[j]:
                answer.append(z)
                break
            else: z += 1
        else: answer.append(z)
    return answer+[0]
