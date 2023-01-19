# https://school.programmers.co.kr/learn/courses/30/lessons/147355
# 5분
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:len(p)+i]) <= int(p):
            answer += 1
    return answer
