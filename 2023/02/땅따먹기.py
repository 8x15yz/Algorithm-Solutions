# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 틀린코드 개오바

def solution(land):
    answer = 0
    mdex = 5
    for ld in land:
        mct = 0
        innermdex = 5
        for i in range(4):
            if i != mdex and mct < ld[i]:
                mct = ld[i]
                innermdex = i
        else:
            answer += mct
            mdex = innermdex
    return answer
