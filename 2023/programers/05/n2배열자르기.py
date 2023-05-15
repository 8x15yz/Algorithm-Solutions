# https://school.programmers.co.kr/learn/courses/30/lessons/87390
# 시간초과되는코드

def solution(n, left, right):
    answer = []
    for i in range(1, n+1):
        ans = []
        for j in range(1, n+1):
            ans.append(max(i, j))
        answer.append(ans)
    newans = []
    for a in answer:
        newans += a
    return newans[left:right+1]
