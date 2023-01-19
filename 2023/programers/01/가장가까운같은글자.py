# https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 10분

def solution(s):
    answer = []
    for i in range(len(s)):
        cnt = -1
        same = []
        for j in range(i):
            if s[i] == s[j]:
                same.append(i-j)
        if len(same) != 0:
            answer.append(min(same))
        else:
            answer.append(cnt)
    return answer
